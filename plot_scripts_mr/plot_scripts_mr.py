import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from vascomodel import utils as vasco_utils


def get_df_from_csv(filename):
    df = pd.read_csv(filename)
    return df


def l_ext_to_int(l_ext):
    return ''  # TODO


def p_ext_to_int(p_ext):
    return ''  # TODO


def get_sales_db_query(db_config, p_id, l_id, start_c_id, end_c_id):
    query = """
        select
            sa_c_id, sa_quantity
        from
            {DB_IDENTIFIER}_CORE.SALES
        join
             {DB_IDENTIFIER}_CORE.calendar
        on
            sa_c_id = c_id
        join
           {DB_IDENTIFIER}_CORE.SALESTYPES
        on
            sa_say_id = say_id
        where
            say_external_code = 'SALE'
        and
            sa_l_id = {LOCATION}
        and
            sa_p_id = {PRODUCT}
        and
            sa_c_id >= {START_C_ID}
        and
            sa_c_id <= {END_C_ID}
        order by
            sa_c_id
        """.format(DB_IDENTIFIER=db_config['db_identifier'],
                   LOCATION=l_id,
                   PRODUCT=p_id,
                   START_C_ID=start_c_id,
                   END_C_ID=end_c_id)
    return query


def get_sales_df_from_db(db_config, p_id, l_id, start_c_id, end_c_id):
    query = get_sales_db_query(db_config, p_id, l_id, start_c_id, end_c_id)
    df = get_df_for_query(db_config, query)
    return df


def get_preds_db_query(db_config, p_id, l_id, ref_c_id, mpg_id):
    query = """
        select
            mpr_c_id,
            mpr_mean
        from
            {DB_IDENTIFIER}_MINING.M_PREDICTIONS
        join
            {DB_IDENTIFIER}_CORE.calendar
        on
            mpr_c_id = c_id
        where
            mpr_mpg_id = {MPG_ID}
        and
             MPR_C_ID_REFERENCE = {REF_C_ID}
        and
            mpr_l_id = {LOCATION}
        and
            mpr_p_id = {PRODUCT}
        order by
            c_id
        """.format(DB_IDENTIFIER=db_config['db_identifier'],
                   LOCATION=l_id,
                   PRODUCT=p_id,
                   REF_C_ID=ref_c_id,
                   MPG_ID=mpg_id)
    return query


def get_sales_csv(sales_file):
    df = get_df_from_csv(sales_file)
    df = df[['sa_c_id', 'sa_quantity']]
    df.rename(columns={'sa_c_id': 'c_id'}, inplace=True)
    return df


def get_preds_csv(preds_file):
    df = get_df_from_csv(preds_file)
    df = df[['mpr_c_id', 'mpr_mean']]
    df.rename(columns={'mpr_c_id': 'c_id'}, inplace=True)
    return df


def get_sales_db(db_config, p_id, l_id, start_c_id, end_c_id):
    df = get_sales_df_from_db(db_config, p_id, l_id, start_c_id, end_c_id)
    df = df[['sa_c_id', 'sa_quantity']]
    df.rename(columns={'sa_c_id': 'c_id'}, inplace=True)
    return df


def get_preds_db(db_config, p_id, l_id, ref_c_id, mpg_id):
    query = get_preds_db_query(db_config, p_id, l_id, ref_c_id, mpg_id)
    df = get_df_for_query(db_config, query)
    df = df[['mpr_c_id', 'mpr_mean']]
    df.rename(columns={'mpr_c_id': 'c_id'}, inplace=True)
    return df


def get_locations_ext2int_dict_from_db(params):
    l_df = get_df_for_query(params, 'select * from {0}_CORE.locations'.format(params['db_identifier']))
    l_ext2int = dict(zip([int(x) for x in l_df.l_external_code.tolist()], l_df.l_l_id_master.tolist()))
    return l_ext2int


def get_products_ext2int_dict_from_db(params):
    p_df = get_df_for_query(params, 'select * from {0}_CORE.products'.format(params['db_identifier']))
    p_ext2int = dict(zip([int(x) for x in p_df.p_external_code.tolist()], p_df.p_p_id_master.tolist()))
    return p_ext2int


def get_df_for_query(params, query):
    """
    An auxiliary function that takes a query and
    returns the corresponding results as a data-frame table.
    """

    engine_string = vasco_utils.EngineString(
        host = params['host_ip'],
        port = params['host_port'],
        username = params['exasol_uid'],
        password = params['exasol_pwd']
        )
    engine = create_engine(engine_string.exasol, echo=False)

    try:
        return pd.read_sql_query(query, engine)
    except:
        pass


def get_sys_params(config):
    """
    Read the system parameter from a given config-file and return them as a dictionary.
    """
    sys_params = {}
    for line in file(config):
        if '=' not in line:
            continue
        fld = line.split('=')
        sys_params[fld[0]] =  fld[1].replace('\n','')
    return sys_params

#########################################################################################
# csv test

# df_sales_csv_test = get_sales_csv('sales.csv')
# df_preds_csv_test = get_preds_csv('preds.csv')
#
# plt.plot(df_sales_csv_test['C_ID'], df_sales_csv_test['SA_QUANTITY'])
# plt.plot(df_preds_csv_test['C_ID'], df_preds_csv_test['MPR_MEAN'])


#########################################################################################
# db real

db_config = get_sys_params('dm_prod_user.cfg')
l_ext2int = get_locations_ext2int_dict_from_db(db_config)
p_ext2int = get_products_ext2int_dict_from_db(db_config)


horizons = range(14, 190, 7)
ref_c_id = 41938
l_ext = 9944
p_ext = 282772


l_id = l_ext2int[l_ext]  # 2889
p_id = p_ext2int[p_ext]  # 31182

start_c_id = ref_c_id + horizons[0]  # 41945+7
end_c_id = ref_c_id + horizons[len(horizons)-1]  # 42134-7

df_sales_db = get_sales_db(db_config, p_id, l_id, start_c_id, end_c_id)
df_preds_1073 = get_preds_db(db_config, p_id, l_id, ref_c_id, 1073)
df_preds_1027 = get_preds_db(db_config, p_id, l_id, ref_c_id, 1027)

plt.plot(df_sales_db['c_id'], df_sales_db['sa_quantity'], '-g', label='sales')
plt.plot(df_preds_1027['c_id'], df_preds_1027['mpr_mean'], '-b', label='1027')
plt.plot(df_preds_1073['c_id'], df_preds_1073['mpr_mean'], '-r', label='1073')

#########################################################################################

plt.show()


# df_full = pd.merge(df_sales, df_preds, on='C_ID')
# print(df_full)