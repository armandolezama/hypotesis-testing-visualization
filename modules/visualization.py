import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

class visualization_module:
  def __init__(self):
    print(self)
  
  def plot_normal_distribution(self, data1):
    mean, std_dev = stats.norm.fit(data1)
    data1Linspace = np.linspace(min(data1), max(data1), 200)
    data1pdf = stats.norm.pdf(data1Linspace, mean, std_dev)

    # mean, std_dev = stats.norm.fit(data2)
    # data2Linspace = np.linspace(min(data1), max(data2), 200)
    # data2pdf = stats.norm.pdf(data2Linspace, mean, std_dev)

    # Grafica la PDF
    plt.figure(figsize=(8, 6))
    # plt.hist(data1, bins=30, density=True, alpha=0.6, color='g', label='Histograma de data1')
    plt.plot(data1Linspace, data1pdf, 'k', linewidth=2, label='Data 1')
    # plt.plot(data2Linspace, data2pdf, 'k', linewidth=2, label='Data 2')
    plt.title('Función de Densidad de Probabilidad (PDF) de data1')
    plt.xlabel('Valores')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.show()