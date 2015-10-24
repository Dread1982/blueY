import pandas as pd
import matplotlib.pyplot as plt


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
            {CORE}.SALES
        join
             {CORE}.calendar
        on
            sa_c_id = c_id
        join
           {CORE}.SALESTYPES
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
        """.format(CORE=db_config['CORE'],
                   LOCATION=l_id,
                   PRODUCT=p_id,
                   START_C_ID=start_c_id,
                   END_C_ID=end_c_id)
    return query


def get_sales_df_from_db(db_config, p_id, l_id, start_c_id, end_c_id):
    query = get_sales_db_query(db_config, p_id, l_id, start_c_id, end_c_id)
    df = get_df_from_query(db_config, query)
    return df


def get_preds_db_query(db_config, p_id, l_id, ref_c_id, mpg_id):
    query = """
        select
            mpr_c_id,
            mpr_mean
        from
            {MINING}.M_PREDICTIONS
        join
            {CORE}.calendar
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
        """.format(CORE=db_config['CORE'],
                   MINING=db_config['MINING'],
                   LOCATION=l_id,
                   PRODUCT=p_id,
                   REF_C_ID=ref_c_id,
                   MPG_ID=mpg_id)
    return query


def get_df_from_query(db_config, query):
    df = None  # TODO
    return df


def get_sales_csv(sales_file):
    df = get_df_from_csv(sales_file)
    df = df[['SA_C_ID', 'SA_QUANTITY']]
    df.rename(columns={'SA_C_ID': 'C_ID'}, inplace=True)
    return df


def get_preds_csv(preds_file):
    df = get_df_from_csv(preds_file)
    df = df[['MPR_C_ID', 'MPR_MEAN']]
    df.rename(columns={'MPR_C_ID': 'C_ID'}, inplace=True)
    return df


def get_sales_db(db_config, p_id, l_id, start_c_id, end_c_id):
    df = get_sales_df_from_db(db_config, p_id, l_id, start_c_id, end_c_id)
    df = df[['SA_C_ID', 'SA_QUANTITY']]
    df.rename(columns={'SA_C_ID': 'C_ID'}, inplace=True)
    return df


def get_preds_db(db_config, p_id, l_id, ref_c_id, mpg_id):
    df = get_preds_db_query(db_config, p_id, l_id, ref_c_id, mpg_id)
    df = df[['MPR_C_ID', 'MPR_MEAN']]
    df.rename(columns={'MPR_C_ID': 'C_ID'}, inplace=True)
    return df


#########################################################################################
# csv test

df_sales_csv_test = get_sales_csv('sales.csv')
df_preds_csv_test = get_preds_csv('preds.csv')

plt.plot(df_sales_csv_test['C_ID'], df_sales_csv_test['SA_QUANTITY'])
plt.plot(df_preds_csv_test['C_ID'], df_preds_csv_test['MPR_MEAN'])


#########################################################################################
# db real

db_config = {'CORE': 'CORE', 'MINING': 'MINING'}

l_id = 2889  # l_ext_to_int(9944)  # TODO
p_id = 31182  # p_ext_to_int(282772) # TODO
start_c_id = 41945+7
end_c_id = 42134-7

ref_c_id = 41938
mpg_id = 1073

# df_sales_db = get_sales_db(db_config, p_id, l_id, start_c_id, end_c_id)
# df_preds_1073 = get_preds_db(db_config, p_id, l_id, ref_c_id, mpg_id)

# plt.plot(df_sales_db['C_ID'], df_sales_db['SA_QUANTITY'])
# plt.plot(df_preds_1073['C_ID'], df_preds_1073['MPR_MEAN'])


#########################################################################################

plt.show()


# df_full = pd.merge(df_sales, df_preds, on='C_ID')
# print(df_full)