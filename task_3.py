# 3)Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

import scipy.stats as stats
import numpy as np

D = 25
M = 174.2
n = 27
a = 0.05

z = 1.96
x_1 = M - z * np.sqrt(D / n)
x_2 = M + z * np.sqrt(D / n)
print(f'Доверительный интервал оценки мат.ожидания роста футболистов'
      f' {[round(x_1, 3), round(x_2, 3)]} с надежностью 0,95')

# print(stats.t.interval(0.95, n-1, loc=174.2))
