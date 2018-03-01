import scipy.stats as scs
import numpy as np
import pandas as pd

class ScipyAdapter():
    '''This is an adapter to make scipy easier to use'''

    def poisson_probability_mass_function(x_values, mean):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda)
            RETURNS: the formula generator (can be passed into         matplotlib

            The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.
        '''
        return scs.poisson.pmf(x_values, mean)

    def poisson_cumulative_distribution_function():
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda)
            RETURNS: the formula generator (can be passed into         matplotlib

            The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.
        '''
        return scs.poisson.cdf(x_values, mean)

    def poisson_stats(mean, moments_str):
        '''
            INPUT: mean (mu, witch hat symble, lambda)
                   moments_str (mvsk or shorter)
            RETURNS: tuple of requested variables (mean, var, skew, kurt)

            mean: 'm' (will be the same as the lambda that was provided)
            variance: 'v'
            skew: 's'
            kurt: 'k'
        '''
        return scs.poisson.stats(mean, moments=moments_str)

    def poisson_random_variables(mean, num_ran_vars):
        '''
            INPUTS: mean (mu, witch hat symble, lambda)
                    num_ran_vars (the number of random varables you want generated)
            RETURNS: the random number generator

            Creates a generator that will create random numbers that generally follow the poisson distribution.
        '''
        return scs.poisson.rvs(mean, size=num_ran_vars)
