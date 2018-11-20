import pandas
from scipy import stats
from math import sqrt
from scipy.stats import t

# Import data
data = pandas.read_csv('D:/python/CLASS2/Handout/EPPY5B08IT6/code/data.csv')

# Run independent t-test
ind_t_test = stats.ttest_ind(data.value[data.names == 'beef'],data.value[data.names == 'pork'])

# Calculate the mean difference and 95% confidence interval
N1 = 30
N2 = 30
df = (N1 + N2 - 2)
std1 = data.value[data.names == 'beef'].std()
std2 = data.value[data.names == 'pork'].std()
std_N1N2 = sqrt( ((N1 - 1)*(std1)**2 + (N2 - 1)*(std2)**2) / df)

diff_mean = data.value[data.names == 'beef'].mean() - data.value[data.names == 'pork'].mean()
MoE = t.ppf(0.975, df) * std_N1N2 * sqrt(1/N1 + 1/N2)

print('The results of the independent t-test are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(ind_t_test[0],ind_t_test[1]))
print ('\nThe difference between groups is {:3.1f} [{:3.1f} to {:3.1f}] (mean [95% CI])'.format(diff_mean, diff_mean - MoE, diff_mean + MoE))