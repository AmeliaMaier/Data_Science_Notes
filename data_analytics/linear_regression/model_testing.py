'''will need'''
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.utils import resample

'''might need'''
from basis_expansions import NaturalCubicSpline
from dftransformers import (ColumnSelector, Identity,
                            FeatureUnion, MapFeature,
                            Intercept)
from regression_helpers import (plot_univariate_smooth,
                                bootstrap_train,
                                display_coef,
                                plot_bootstrap_coefs,
                                plot_partial_depenence,
                                plot_partial_dependences,
                                predicteds_vs_actuals)
from math import ceil
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

'''
QQ Plot is Actual vs Predicted

Assumptions that should be considered for Linear Regression

1. sample data is representive of the population
    -how was it gathered
    -has anything been added/removed
    ...
2. True relationship between X and y is linear.
    -does the data need to be transformed to create linear relationship
    -would a different model type work better?
3. Feature matrix X has full rank
    - rows and columns are linearly independent
    - if not, do you drop the some data or account for it
    * Tested with correlation matrix for features
4. Residuals are independent
5. Residuals are normally distributed.
    - 4 and 5 usually tested together
    * On a QQ plot, residuals are evenly distributed above and below the line
6. Variance of the residuals is constant
    -homoscedastic
    * On a QQ plot the residuals do not fan
'''

def rss(y_found, y_estimated):
    '''
        INPUT: dataframe of real data, dataframe of predicted data
        RETURN: numeric RSS value
        In statistics, the residual sum of squares (RSS), also known as the sum of squared residuals (SSR) or the sum of squared errors of prediction (SSE), is the sum of the squares of residuals (deviations predicted from actual empirical values of data). It is a measure of the discrepancy between the data and an estimation model. A small RSS indicates a tight fit of the model to the data. It is used as an optimality criterion in parameter selection and model selection.
    '''
    return np.sum((y_found - y_estimated)**2)

def rsq(y_found, y_hat):
    '''
        INPUT: dataframe of real data, dataframe of predicted data
        RETURN: numeric R squared value
        In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variance in the dependent variable that is predictable from the independent variable(s)
    '''
    ss_tot = rss(y_found, np.mean(y_found))
    ss_res = rss(y_found, y_estimated)
    return 1 - (ss_res / ss_tot)

def bootstrap_rsq(X_found, y_found, pipeline, n_boot=10000):
    '''
        INPUT: dataframe of real data X, dataframe of real data Y, transformation pipeline, number of samples to pull
        RETURN: list of numeric R squared values
        In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variance in the dependent variable that is predictable from the independent variable(s)
        Bootstraping allows for the creation of n_boot number of R squared values for the data to show us how much variance is in our R squared value and put a confidance interval around it.
    '''
    rsqs = []
    for _ in range(n_boot):
        X_boot, y_boot = resample(X_found, y_found)
        X_transform = pipeline.transform(X_boot)
        model = LinearRegression(fit_intercept=False)
        model.fit(X_transform.values, y_boot)
        y_boot_hat = model.predict(X_transform.values)
        rsqs.append(rsq(y_boot, y_boot_hat))
    return rsqs

def plot_partial_dependences_example():
    '''
        This method is not intended to be run, it is an example of how to use the method that was provided to us.
        To be used after fitting a model to check which variables are helping with the prediction and which aren't.
        It will print a plot for each var_name. You are looking for a linear relationship: if the line has no slope, it is probably not helping with the model and can be removed. A positive or negative slope means it effects the model's prediction in some way.
    '''
    fig, axs = plot_partial_dependences(
         balance_model,
         X=balance_non_zero,
         var_names=['Income', 'Rating', 'Age'],
         pipeline=balance_pipeline,
         #bootstrap_models=bootstrap_models,
         y=balance_non_zero["Balance"])
    fig.tight_layout()
    plt.show()

def plot_bootstraped_coefficient_estimates_example():
    '''
        This method is not intended to be run, it is an example of how to use the method that was provided to us.
        To be used after fitting a model to check which variables are reliably being used.
        It will print a plot for each feature. You are looking for features that center around zero. If that is the case then the model isn't actually sure it should be used (note: look at all the splines for the given feature before removing it). If the 95% confidance interval includes zero for all splines of a feature, consider removing it and seeing how the model looks afterwards.
    '''
    bootstrap_models = bootstrap_train(
    LinearRegression,
    balance_features.values,
    balance_non_zero["Balance"].values,
    fit_intercept=False,
    bootstraps=10000
    )
    fig, axs = plot_bootstrap_coefs(bootstrap_models, balance_features.columns, n_col=2)
    fig.tight_layout()
    plt.show()

def residual_plot(ax, x, y, y_hat, n_bins=50):
    residuals = y - y_hat
    ax.axhline(0, color="black", linestyle="--")
    ax.scatter(x, residuals, color="grey", alpha=0.5)
    ax.set_ylabel("Residuals ($y - \hat y$)")
def plot_residuals_example():
    '''
        This method is not intended to be run, it is an example of how to use the method that was provided to us.
        To be used after fitting a model to check which variables are reliably being used.
        It will print a plot of the residuals of a variable (to be run on each feature and the Y) around zero. You are looking for any graphs that show asymetry across zero. This is a sign of heteroskedasity and that the model is not going to predict well.
    '''
    fig, ax = plt.subplots(figsize=(14, 3))
    residual_plot(ax, y_hat, balance_non_zero["Balance"], y_hat)
    ax.set_title("log(Balance) vs. Predicted Value")

def plot_predicted_vs_actuals_example():
    '''
        This method is not intended to be run, it is an example of how to use the method that was provided to us.
        To be used after fitting a model to check which variables are reliably being used.
        It will print a plot of the predicted values in red and the actuals in grey for a variable (to be run on each feature and the Y). See how well it fits or doesn't fit.
    '''
    fig, ax = plt.subplots(figsize=(14, 3))
    predicteds_vs_actuals(ax, balance_non_zero["Income"], balance_non_zero["Balance"], y_hat)
    ax.set_title("log(Balance) vs. Income")
