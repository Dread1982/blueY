from __future__ import print_function, division
import pickle
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.cross_validation import train_test_split
from nbpy import flags, x_transformer, neurobayes, nclassify, pipeline, meta_estimator, on_cols
import nbpy.matplotlib_plotting as mplot
from sklearn.neighbors import KNeighborsRegressor
from nbpy.ext import predict_as_transform, plots
from sklearn.ensemble import GradientBoostingClassifier


def prepare_features(X, fit_mode, feature_properties):
    """Prepare the features for the California Housing project and set
    the feature properties for Neurobayes.
    """
    for column in ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                   'Population', 'AveOccup', 'Longitude', 'Latitude']:
        feature_properties[column] = flags.IS_CONTINUOUS

    # no additional features so far...
    feature_properties['BedroomsToTotalRooms'] = flags.IS_CONTINUOUS
    X['BedroomsToTotalRooms'] = X['AveBedrms'] / X['AveRooms']

    feature_properties['avg_of_nearest_neighbors'] = flags.IS_CONTINUOUS
    del X['Latitude']
    del X['Longitude']

    return X


def create_pipeline():
    feature_properties = {}

    MIN_PERCENTAGE = 0.03

    nearest_neighbors = KNeighborsRegressor()
    nearest_neighbors = predict_as_transform.PredictAsTransform(
        ('avg_of_nearest_neighbors', nearest_neighbors))

    nearest_neighbors = on_cols.OnCols(('Latitude', 'Longitude'), nearest_neighbors)

    preparer = x_transformer.CustomXTransformerFP(
        prepare_features, feature_properties=feature_properties)

    # classifier = neurobayes.NeurobayesClassifier(
    #    feature_properties=feature_properties, histogram_data=True)

    classifier = GradientBoostingClassifier(
      n_estimators=100,
      learning_rate=0.1,
      max_depth=3,
      random_state=1)

    nclassify_estimator = nclassify.NClassify(
        classifier, min_percentage=MIN_PERCENTAGE)

    return pipeline.Pipeline([
        ('nearest_neighbors', nearest_neighbors),
        ('prepare_features', preparer),
        ('nclassify', nclassify_estimator),
        ])


def create_train_and_test_data(cal_housing):
    X_train, X_test, y_train, y_test = train_test_split(cal_housing.data, cal_housing.target)
    X_train = pd.DataFrame(X_train, columns=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                                             'Population', 'AveOccup', 'Longitude', 'Latitude'])
    X_test = pd.DataFrame(X_test, columns=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                                           'Population', 'AveOccup', 'Longitude', 'Latitude'])

    return X_train, X_test, y_train, y_test


def fit_and_predict(pipe, X_train, y_train, X_test):
    pipe.fit(X_train, y_train)

    pipe.get_subestimators()

    pred = pipe.predict(X_test, actions=[pipe.mean_action(), pipe.median_action()])
    return pred


def is_nclassify(key, subest):
    return isinstance(subest, nclassify.NClassify)


def print_mad_for_mean_and_median(pred, y_test):
    mad_mean = np.abs(y_test - pred['mean']).mean()
    mad_median = np.abs(y_test - pred['median']).mean()
    print("mean absolute deviation of the mean prediction: " + str(mad_mean))
    print("mean absolute deviation of the median prediction: " + str(mad_median))


def training_tree_and_analysis_plot(pipe):
    nclassify_est = meta_estimator.search_subestimators_in_tree(pipe, is_nclassify)[0][-1]
    # nclassify_est.plot_tree()
    # plt.show()

    classifiers = nclassify_est.get_classifiers_sorted_by_percentage()
    name, sub_est = classifiers[0]
    # my_plotting_instance = mplot.Plotting(sub_est)
    # filename = 'analysis_plots' + str(name)
    # my_plotting_instance.plot_analysis(filename, sorting='importance')


def execute():
    cal_housing = fetch_california_housing()

    X_train, X_test, y_train, y_test = create_train_and_test_data(cal_housing)

    pipe = create_pipeline()

    pred = fit_and_predict(pipe, X_train, y_train, X_test)

    print_mad_for_mean_and_median(pred, y_test)

    training_tree_and_analysis_plot(pipe)

    fileObject = open("pickle_test", 'wb')
    pickle.dump(pipe, fileObject)
    fileObject.close()

    fileObject = open("pickle_test", 'r')
    unpickled_pipe = pickle.load(fileObject)

    pred_unpickled = fit_and_predict(unpickled_pipe, X_train, y_train, X_test)

    print_mad_for_mean_and_median(pred_unpickled, y_test)


if __name__ == "__main__":
    execute()