import numpy as np
from scipy import stats

class data_generator:
  def __init__(self) -> None:
    self.fixed_data = {
      'Q1_t-test_independent' : {
        'sync' : np.array([94. , 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]),
        'asyncr' : np.array([77.1, 71.7, 91. , 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]),
      }
    }
  
  def get_normal_data_simulation(self, data, sample_size):
    mean, std_dev = stats.norm.fit(data)

    error = data - mean

    simulated_data = np.random.normal(loc=mean, scale=std_dev, size=sample_size)

    error_indices = np.random.choice(range(len(error)), size=sample_size, replace=True)

    simulated_data += error[error_indices]

    return simulated_data
  