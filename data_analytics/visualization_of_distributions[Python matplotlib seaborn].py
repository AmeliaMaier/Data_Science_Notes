import scipy.stats as scs
import matplotlib.pyplot as plt
import numpy as np

## A typist makes on average 2 mistakes per page.
#What is the probability of a particular page having no errors on it?
'''Poisson  poisson.pmf(k) = exp(-mu) * mu**k / k!'''
'X = Poisson(lamda=2)'

## declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10,6),dpi=300)
splot = 0

## loop through parameterizations of the beta
for lamb in [2.0]:
    splot += 1
    ax = fig.add_subplot(2,3,1)

    x = np.arange(scs.poisson.ppf(0.01, lamb),scs.poisson.ppf(0.99, lamb))
    ax.plot(x, scs.poisson.pmf(x, lamb), 'bo', ms=8, label='pmf')
    ax.vlines(x, 0, scs.poisson.pmf(x, lamb), colors='b', lw=5, alpha=0.5)
    rv = scs.poisson(lamb)

    ax.set_xlim((-0.5,10.5))
    ax.set_ylim((0,0.6))
    ax.set_title("lambda=%s"%(lamb))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
#plt.savefig("poisson.png",dpi=400)
print(rv.pmf(0))

#Components are packed in boxes of 20. The probability of a component being defective is 0.1.
#What is the probability of a box containing 2 defective components?
'''Binomial '''
# looxp through parameterizations of the beta
for n, p in [(20,0.1)]:
    splot += 1
    ax2 = fig.add_subplot(2, 3, 2)

    x = np.arange(scs.binom.ppf(0.01, n, p), scs.binom.ppf(.99, n, p)+1)
    ax2.plot(x, scs.binom.pmf(x, n, p), 'bo', ms=8, label='pmf')
    ax2.vlines(x, 0, scs.binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    rv = scs.binom(n, p)

    ax2.set_ylim((0, 1.0))
    ax2.set_xlim((-0.5, 5.5))
    ax2.set_title("n=%s,p=%s" % (n, p))
    ax2.set_aspect(1./ax2.get_data_ratio())

    for t in ax2.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax2.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)

rv = scs.binom(20,0.1)
print(rv.pmf(2))

#Patrons arrive at a local bar at a mean rate of 30 per hour.
#What is the probability that the bouncer has to wait more than 3 minutes to card the next patron?
'''Exponential'''

## loop through parameterizations of the beta
for lamb in [0.5]:
    splot += 1
    scale = 1./lamb

    rv = scs.expon(scale=scale)
    r = scs.expon.rvs(size=1000,scale=scale)
    pdf_range = np.linspace(scs.expon.ppf(0.0001),scs.expon.ppf(0.9999), 100)

    ax4 = fig.add_subplot(2,3,3)
    ax4.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,normed=1,histtype='stepfilled')
    ax4.plot(pdf_range, rv.pdf(pdf_range),'#FF0099', lw=5, label='pdf')
    ax4.set_xlim((0,12))
    ax4.set_ylim((0,1.0))
    ax4.set_title("lambda=%s"%(lamb))
    ax4.set_aspect(1./ax4.get_data_ratio())

    for t in ax4.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax4.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
print(1-rv.cdf(3))

#A variable is normally distributed with a mean of 120 and a standard deviation of 5. One score is randomly sampled.
#What is the probability the score is above 127? Use scipy.stats.norm to perform the calculation.
'''Normal'''

## loop through parameterizations of the beta
for mu,sig in [(120,5)]:
    splot += 1
    ax3 = fig.add_subplot(2,3,4)

    rv = scs.norm(loc=mu,scale=sig)
    r = scs.norm.rvs(size=1000,loc=mu,scale=sig)
    pdf_range = np.linspace(scs.norm.ppf(0.01),scs.norm.ppf(0.99), 100)

    ax3.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,normed=1,histtype='stepfilled')
    pdf_range = np.linspace(scs.norm.ppf(0.0001, mu, sig),scs.norm.ppf(0.9999, mu, sig), 100)
    ax3.plot(pdf_range, rv.pdf(pdf_range),'#FF0099', lw=4, label='pdf')
    ax3.set_title("mu=%s, sigma=%s"%(mu,sig))
    ax3.set_aspect(1./ax3.get_data_ratio())

    for t in ax3.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax3.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
print(1-rv.cdf(127))

#You need to find a tall person, at least 6 feet tall, to help you reach a cookie jar. 8% of the population is 6 feet or taller.
#If you wait on the sidewalk, how many people would you expect to have passed you by before you'd have a candidate to reach the jar?
'''Geometric'''
rv = scs.geom(p=.08)
print(rv.mean()) #print mean

#A harried passenger will be several minutes late for a scheduled 10 A.M. flight to NYC. Nevertheless, he might still make the flight, since boarding is always allowed until 10:10 A.M., and boarding is sometimes permitted up to 10:30 AM.
#Assuming the extended boarding time is uniformly distributed over the above limits, find the probability that the passenger will make his flight, assuming he arrives at the boarding gate at 10:25.
'''uniform'''

a=10
b=30
x=25
rv = scs.uniform(10,20)

print(1-rv.cdf(25))

plt.show()
