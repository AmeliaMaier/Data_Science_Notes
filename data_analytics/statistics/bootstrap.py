from data_visualization/basic_matplotlib import plot_histogram as plot
import numpy as np

'''https://stats.stackexchange.com/questions/26088/explaining-to-laypeople-why-bootstrapping-works
https://www.youtube.com/watch?v=_nhgHjdLE-I'''

def bootstrap(sample_array, resample=10000):
    '''Implement a bootstrap function to randomly draw with replacement from a given sample. The function should take a sample as a numpy ndarray and the number of resamples as an integer (default: 10000). The function should return a list of numpy ndarray objects, each ndarray is one bootstrap sample.'''
    samples = []
    sample_array=sample_array.ravel()
    for num in range(resample):
        samples.append(np.random.choice(sample_array, len(sample_array)))
    return samples

def bootstrap_ci(sample, stat_function=np.mean, iterations=1000, ci=95):
    '''Implement a bootstrap_ci function to calculate the confidence interval of any sample statistic (in this case the mean). The function should take a sample, a function that computes the sample statistic, the number of resamples (default: 10000), and the confidence interval (default :95%). The function should return the lower and upper bounds of the confidence interval and the bootstrap distribution of the test statistic.'''
    sample_lst = bootstrap(sample, iterations)
    results = []
    for sample_set in sample_lst:
        results.append(stat_function(sample_set))
    results.sort()
    results = np.array(results)

    '''this does the same as the np.percentile under it'''
    #results_cut = results[int((len(results)*((1-(ci/100))/2))):int(len(results)-(len(results)*((1-(ci/100))/2)))]

    plot(results)
    return (np.percentile(results, q=[(100-ci)/2,100-(100-ci)/2]), stat_function(results))
