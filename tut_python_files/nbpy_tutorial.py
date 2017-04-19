from __future__ import print_function, division
import logging
import sys
import numpy as np
import pandas as pd
from nbpy.datasets import fetch_data
from nbpy.x_transformer import MultiLabelEncoder
from nbpy import flags
from nbpy.neurobayes import NeurobayesClassifier
from nbpy.matplotlib_plotting import Plotting


def add_logger():
    logger = logging.getLogger("nbpy")
    formatter = logging.Formatter('[NeuroBayes:%(levelname)s] %(message)s')
    streamhdlr = logging.StreamHandler(sys.stderr)
    streamhdlr.setFormatter(formatter)
    logger.setLevel(logging.CRITICAL)
    logger.addHandler(streamhdlr)


def load_train_data():
    X, y = fetch_data('adult_census_train')
    # print(X.shape)  # 32561, 14
    # print(X.dtypes)
    # all object type features

    return X, y


def convert_native_country_column(X):
    is_us = X['native_country'] == 'United-States'
    not_us_not_na = (X['native_country'] != 'United-States') & (pd.isnull(X['native_country']) == False)
    X.loc[is_us, 'native_country'] = 1
    X.loc[not_us_not_na, 'native_country'] = 0
    X['native_country'] = X['native_country'].astype(float)


def transform_object_columns(X):
    trans = MultiLabelEncoder(
        selected_columns=['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'sex'],
        mappings={'education': ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th',
                                '12th', 'HS-grad', 'Some-college', 'Assoc-voc', 'Assoc-acdm',
                                'Bachelors', 'Masters', 'Prof-school', 'Doctorate']})
    trans.fit(X.copy())
    X_trans = trans.transform(X.copy())

    # print(X_trans['race'].unique())  # [ 4.  2.  1.  0.  3.]

    return X_trans


def get_feature_properties():
    """
    age                 int64
    workclass         float64
    fnlwgt              int64
    education         float64
    education_num       int64
    marital_status    float64
    occupation        float64
    relationship      float64
    race              float64
    sex               float64
    capital_gain        int64
    capital_loss        int64
    hours_per_week      int64
    native_country    float64
    """
    feature_properties = {'age': flags.IS_ORDERED,
                          'workclass': flags.IS_UNORDERED | flags.HAS_MISSING,
                          'fnlwgt': flags.IS_CONTINUOUS,
                          'education': flags.IS_ORDERED,
                          'education_num': flags.IS_ORDERED,
                          'marital_status': flags.IS_UNORDERED,
                          'occupation': flags.IS_UNORDERED | flags.HAS_MISSING,
                          'relationship': flags.IS_UNORDERED,
                          'race': flags.IS_UNORDERED,
                          'sex': flags.IS_UNORDERED,
                          'capital_gain': flags.IS_UNORDERED,
                          'capital_loss': flags.IS_UNORDERED,
                          'hours_per_week': flags.IS_ORDERED,
                          'native_country': flags.IS_UNORDERED | flags.HAS_MISSING}

    return feature_properties


if __name__ == "__main__":

    # exercise 2
    add_logger()

    # exercise 3
    X, y = load_train_data()

    # exercise 4
    convert_native_country_column(X)

    # exercise 5
    X_trans = transform_object_columns(X)

    # exercise 6
    feature_properties = get_feature_properties()

    # exercise 7
    clsf = NeurobayesClassifier(histogram_data=True, feature_properties=feature_properties)

    # exercise 8
    clsf.fit(X_trans, y)

    # exercise 9
    # print(clsf.significance_table_)
    # feature "education_num" was removed
    # column "added_significance" is used for the significance cut
    # column "only_this" computation does not take into account other features

    # exercise 10
    plt = Plotting(clsf)
    # plt.plot_analysis()


    """
     1) occupation: 1843 missing, native_country: 583, workclass: 1836
     2) 17, 90
     3) in marital_status, 2.0 has the highest signal rate
     4) In general, the Gini coefficient measures the inequality among values of a statistical distribution. High
        inequality is desired in this context, because we want the 'income', i.e. the true signal cases, to concentrate
        among the samples with the highest estimated signal probability.
     5) The target profile consists of the mean target values in each feature bin (see the black dots with the error
        bars). These mean values are then regularized (shown in red).
     6) When the feature only has a weak correlation to the target
     7) - fit of orthogonal polynomials (for continuous)
        - taking the other signal rate values as a prior (for ordered)
        - all the other signal rates as a prior (for unordered)
    """


    # exercise 11
    X_test, y_test = fetch_data('adult_census_test')
    convert_native_country_column(X_test)
    X_test_trans = transform_object_columns(X_test)

    # exercise 12
    pred = clsf.predict(X_test_trans)
    proba = clsf.predict_proba(X_test_trans)
    print(proba)

    mae = np.mean(np.abs(pred - y_test))
    print(mae)