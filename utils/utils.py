import pandas as pd
import statsmodels.api as sm

def demand(price: pd.Series, demand: pd.Series, method: str = "linear", verbose: bool = False):
    ''' Fits the average demand as a function of price.
    Args:
        price (pd.Series): Series of prices.
        demand (pd.Series): Series of demand.
        method (str): Method to fit the demand curve. Options are "linear".
        verbose (bool): If True, prints the summary of the model.'''
    X = price
    y = demand
    if method == "linear":
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        if verbose:
            print(model.summary())
    
    return model