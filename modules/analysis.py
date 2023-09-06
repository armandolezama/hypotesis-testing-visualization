import scikit_posthocs as sp
from scipy import stats
import pandas as pd
pd.options.display.float_format = '{:,.4f}'.format

class testing_analyzer:

  def __init__(self):
    print(self)

  def check_normality(self, data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
      print("Reject null hypothesis >> The data is not normally distributed")
    else:
      print("Fail to reject null hypothesis >> The data is normally distributed")       

  def check_variance_homogeneity(self, group1, group2):
    test_stat_var, p_value_var= stats.levene(group1,group2)
    print("p value:%.4f" % p_value_var)
    if p_value_var <0.05:
      print("Reject null hypothesis >> The variances of the samples are different.")
    else:
      print("Fail to reject null hypothesis >> The variances of the samples are same.")
  
  def run_t_test_independent(self, sample1, sample2):
    ttest,p_value = stats.ttest_ind(sample1,sample2)
    print("p value:%.8f" % p_value)
    print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
    if p_value/2 <0.05:
        print("Reject null hypothesis")
    else:
        print("Fail to reject null hypothesis") 