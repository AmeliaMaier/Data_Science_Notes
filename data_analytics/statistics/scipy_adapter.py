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

    def exponential_probability_density_function(x_values):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
            RETURNS: the formula generator (can be passed into         matplotlib

            In probability theory and statistics, the exponential distribution (also known as negative exponential distribution) is the probability distribution that describes the time between events in a Poisson point process, i.e., a process in which events occur continuously and independently at a constant average rate.
        '''
        return scs.expon.pdf(x_values)

    def exponential_cumulative_distribution_function(x_values):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda)
            RETURNS: the formula generator (can be passed into         matplotlib

            In probability theory and statistics, the exponential distribution (also known as negative exponential distribution) is the probability distribution that describes the time between events in a Poisson point process, i.e., a process in which events occur continuously and independently at a constant average rate.
        '''
        return scs.expon.cdf(x_values)

    def exponential_stats(moments_str):
        '''
            INPUT: moments_str (mvsk or shorter)
            RETURNS: tuple of requested variables (mean, var, skew, kurt)

            mean: 'm' (will be the same as the lambda that was provided)
            variance: 'v'
            skew: 's'
            kurt: 'k'
        '''
        return scs.expon.stats(moments=moments_str)

    def exponential_random_variables(num_ran_vars):
        '''
            INPUTS: num_ran_vars (the number of random varables you want generated)
            RETURNS: the random number generator

            Creates a generator that will create random numbers that generally follow the poisson distribution.
        '''
        return scs.expon.rvs(size=num_ran_vars)

    def gamma_probability_density_function(x_values, mean):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda, alpha)
            RETURNS: the formula generator (can be passed into         matplotlib

            In probability theory and statistics, the gamma distribution is a two-parameter family of continuous probability distributions. The exponential distribution, Erlang distribution, and chi-squared distribution are special cases of the gamma distribution. There are three different parametrizations in common use:

            With a shape parameter k and a scale parameter θ.
            With a shape parameter α = k and an inverse scale parameter β = 1/θ, called a rate parameter.
            With a shape parameter k and a mean parameter μ = k/β.

            In each of these three forms, both parameters are positive real numbers.

            The gamma distribution is the maximum entropy probability distribution (both with respect to a uniform base measure and with respect to a 1/x base measure) for a random variable X for which E[X] = kθ = α/β is fixed and greater than zero, and E[ln(X)] = ψ(k) + ln(θ) = ψ(α) − ln(β) is fixed (ψ is the digamma function)

            In most cases, the gamma function in scipy can be simplified to just take x_values and mean.
        '''
        return scs.gamma.pdf(x_values, mean)

    def gamma_cumulative_distribution_function(x_values, mean):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda, alpha)
            RETURNS: the formula generator (can be passed into         matplotlib

            In probability theory and statistics, the gamma distribution is a two-parameter family of continuous probability distributions. The exponential distribution, Erlang distribution, and chi-squared distribution are special cases of the gamma distribution. There are three different parametrizations in common use:

            With a shape parameter k and a scale parameter θ.
            With a shape parameter α = k and an inverse scale parameter β = 1/θ, called a rate parameter.
            With a shape parameter k and a mean parameter μ = k/β.

            In each of these three forms, both parameters are positive real numbers.

            The gamma distribution is the maximum entropy probability distribution (both with respect to a uniform base measure and with respect to a 1/x base measure) for a random variable X for which E[X] = kθ = α/β is fixed and greater than zero, and E[ln(X)] = ψ(k) + ln(θ) = ψ(α) − ln(β) is fixed (ψ is the digamma function)

            In most cases, the gamma function in scipy can be simplified to just take x_values and mean.
        '''
        return scs.gamma.cdf(x_values, mean)

    def gamma_stats(mean, moments_str):
        '''
            INPUT: mean (mu, witch hat symble, lambda, alpha)
                   moments_str (mvsk or shorter)
            RETURNS: tuple of requested variables (mean, var, skew, kurt)

            mean: 'm' (will be the same as the lambda that was provided)
            variance: 'v'
            skew: 's'
            kurt: 'k'
        '''
        return scs.gamma.stats(mean, moments=moments_str)

    def gamma_random_variables(mean, num_ran_vars):
        '''
            INPUTS: mean (mu, witch hat symble, lambda, alpha)
                    num_ran_vars (the number of random varables you want generated)
            RETURNS: the random number generator

            Creates a generator that will create random numbers that generally follow the poisson distribution.
        '''
        return scs.gamma.rvs(mean, size=num_ran_vars)

    def normal_probability_density_function(x_values):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
            RETURNS: the formula generator (can be passed into         matplotlib

            Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known
        '''
        return scs.norm.pdf(x_values)

    def normal_cumulative_distribution_function(x_values):
        '''
            INPUTS: x_values (the bins at the bottom of the graph)
                     mean (mu, witch hat symble, lambda)
            RETURNS: the formula generator (can be passed into         matplotlib

            Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known
        '''
        return scs.norm.cdf(x_values)

    def normal_stats(moments_str):
        '''
            INPUT: moments_str (mvsk or shorter)
            RETURNS: tuple of requested variables (mean, var)

            mean: 'm' (will be the same as the lambda that was provided)
            variance: 'v'
        '''
        return scs.norm.stats(moments=moments_str)

    def normal_random_variables(num_ran_vars):
        '''
            INPUTS: num_ran_vars (the number of random varables you want generated)
            RETURNS: the random number generator

            Creates a generator that will create random numbers that generally follow the poisson distribution.
        '''
        return scs.norm.rvs(size=num_ran_vars)
