import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('D:\Programs\PyCharm\pythonProject\ErrorTester2.0\error_approximation\experiments\experiment_16_p_1.txt',
                     header=None, sep='\t')
df.columns = ['T', 'Vin_dT/T', 'Vin_de/e', 'Hybr_dT/T', 'Hybr_de/e', 'Matr_dT/T', 'Matr_de/e', '2d_dT/T', '2d_de/e']
df = df.set_index(df.columns[0])
plt.show()

# from abc import ABC, abstractmethod
import pdb
# class Car:
#     def __init__(self):
#         print('Car created')
#
#
# class Bmv(Car):
#     def __init__(self):
#         super().__init__()
#         print(f'{self.__class__} created')
#
#
# b = Bmv()
