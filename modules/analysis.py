import scikit_posthocs as sp
import numpy as np
from scipy import stats
import pandas as pd
pd.options.display.float_format = '{:,.4f}'.format

class testing_analyzer:

  def __init__(self):
    print(self)

  def check_normality(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
      print("Reject null hypothesis >> The data is not normally distributed")
    else:
      print("Fail to reject null hypothesis >> The data is normally distributed")       

  def check_variance_homogeneity(group1, group2):
    test_stat_var, p_value_var= stats.levene(group1,group2)
    print("p value:%.4f" % p_value_var)
    if p_value_var <0.05:
      print("Reject null hypothesis >> The variances of the samples are different.")
    else:
      print("Fail to reject null hypothesis >> The variances of the samples are same.")