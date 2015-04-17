from __future__ import print_function, division
import numpy as np
import pandas as pd
import datetime


def create_series():
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print(s)

    d = {'a': 1, 'b': 2, 'c': 3}
    s2 = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s2)

    s3 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
    print(s3)


def create_data_frames():
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)
    print(df)

    d2 = {'one': [1., 2., 3., 4.],
          'two': [4., 3., 2., 1.]}
    df2 = pd.DataFrame(d2)
    print(df2)

    d3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
    df3 = pd.DataFrame(d3)
    print(df3)


def create_data_frame_from_csv():
    df = pd.read_csv('./product_1.csv', sep=';')
    print("column names: " + str(df.columns))

    #df = df.reindex(index=df.index + 1, columns=list(df.columns) + ['E'])
    #print(df.index)

    df = df.fillna(value=0)

    print("unique colors: " + str(df['color'].unique()))

    average_sale = np.mean(df['sale'])
    print("average sale: " + str(average_sale))

    df['diff_sale_avg'] = np.abs(df['sale'] - average_sale)

    print(df)


def load_products_data_frames():
    df = pd.read_csv('./product_1.csv', sep=';')
    df2 = pd.read_csv('./product_2.csv', sep=';')
    df3 = pd.read_csv('./product_3.csv', sep=';')
    df = df.append(df2, ignore_index=True)
    df = df.append(df3, ignore_index=True)
    return df


def add_promotion_column(df):
    is_blue_shirt = (df['product'] == "T-Shirt") & (df['color'] == "blue")
    df['promotion'] = 0
    df['promotion'][is_blue_shirt] = 1


def blue_shirts_promotion():
    df = load_products_data_frames()

    add_promotion_column(df)

    print(df)


def erase_black_jeans(df):
    df = df[(df['product'] != 'Jeans') | (df['color'] != 'black')]
    return df


def load_df_and_erase_black_jeans():
    df = load_products_data_frames()

    df = erase_black_jeans(df)

    print(df)


def f(x):
    return x[4]


def merge_with_predictions():
    df = load_products_data_frames()

    add_promotion_column(df)

    df2 = pd.read_csv('./prediction.csv', sep=';')

    df = pd.merge(df, df2, how='outer')

    df = df.fillna(value=0)

    df = erase_black_jeans(df)

    df['diff_sale_prediction'] = np.abs(df['sale'] - df['prediction'])
    group_by_product_color = df.groupby(['product', 'color'])

    d = {'mean_sale': group_by_product_color['sale'].mean(),
         'mean_prediction': group_by_product_color['prediction'].mean(),
         'MAD': (group_by_product_color['diff_sale_prediction']).mean()}
    df_grouped = pd.DataFrame(d)

    # print(df_grouped)

    sales_per_day = df[df['promotion'] == 0].groupby('date')['sale'].sum()
    sales_per_day.sort()
    sales_per_day = sales_per_day[::-1]

    # print(sales_per_day)

    pd.set_printoptions(max_columns=10)

    # df['prediction_naive'] = df['sale'].shift(1)

    # print(df[df['product'] == 'Jeans'])

    df['date'] = df['date'].apply(lambda dt: datetime.datetime.strptime(dt, "%Y-%m-%d"))

    # df.set_index('date')

    df['sale'].plot()

merge_with_predictions()