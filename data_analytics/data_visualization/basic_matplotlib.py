import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import HTML, Image
from sklearn import datasets

'''https://www.kdnuggets.com/2017/01/datascience-data-visualization-matplotlib.html'''

class BasicMatplotlib():
    '''Code examples of basic graphs in matplotlib'''
    '''command
        plot            plot lines and/or markers
        bar             bar plot
        error bar       error bar plot
        boxplot         boxplot
        histogram       histogram
        pie             pie charts
        imshow          heatmaps/images
        scatter         scatter plots'''


    def plot_histogram(data):
        '''simplest form of a histogram'''
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111)
        ax.hist(data, normed=True)
        plt.show()

    def plot_histogram_of_means(dist, params, repeat, size=200):
        """
        Now that you are comfortable drawing samples from various distributions, let's explore some behaviour of samples. Implement a plot_means function that takes the same arguments as make_draws() but adds an extra argument repeat which determines the number of times to redraw a random sample of size from the distribution (and then plots the means). (Since make_draws instantiates a distribution object each time it is called and this involves quite a bit of overhead, for the sake of efficiency DO NOT just call make_draws from the plot_means function, but rather directly create the necessary functionality from scratch.)
        """
        #set up variables
        max_arr = []
        for num in range(repeat):
            #draws samples of random variables from a spefified distribution with given parameters and adds them to an array
            max_arr.append(dist(**params).rvs(size).max())
        #create drawing area
        fig = plt.figure(figsize=(10,10))
        #add a single axie to the figure (211) or (121) for adding one of two (212) or (122) for the second one
        ax = fig.add_subplot(111)
        #pass in the column of data you want a histogram of, always norm the data in a histogram
        ax.hist(max_arr, normed=True)
        #print the graph to the screen, nothing after plt.show() will run until the graph is closed
        plt.show()

class twelve_graphs_histogram_with_two_lines_each():
    fig, axes = plt.subplots(4,3, figsize=(15,10))
    rainfall_df = pd.read_csv("dsi-estimation-sampling/data/rainfall.csv")

    def each_graph(month, ax):
        histogram = ax.hist(rainfall_df[month].values, normed=True)
        rain_range = list(range(int(rainfall_df[month].values.max())+1))
        mean_rainfall = rainfall_df[month].values.mean()
        var_rainfall = rainfall_df[month].values.std()
        poison = stats.poisson.pmf(rain_range, mean_rainfall)
        poisson_line =ax.plot(rain_range, poison, label='poisson pmf', color='r')
        gamma = stats.gamma.pdf(rain_range,mean_rainfall)
        gamma_line = ax.plot(rain_range, gamma, label='gama pdf', color='c')

    axes = axes.ravel()
    count = 0
    for column in rainfall_df:
        if count == 0:
            count += 1
            continue
        each_graph(column, axes[count-1])
        count +=1

    plt.legend()
    plt.tight_layout()
    plt.show()

class iris():

	def iris_scatter_matrix():
	    iris = datasets.load_iris()
	    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
	    data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
	    pd.plotting.scatter_matrix(data, figsize=(12,12))
	    plt.show()

	def iris_scatter_matrix_seaborn():
	    import seaborn as sns
	    sns.set(style="ticks", color_codes=True)
        g = sns.pairplot(data, hue="species", palette="husl")
        plt.show()
