# -*- coding: utf-8 -*-
import numpy as np


def combination(n: int, k: int):
    return np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n - k)


# %%
# 1. Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std,
# var, mean) среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

salary = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65,
          84, 90, 150])
N = len(salary)
salary_average = sum(salary)/len(salary)
sqrt_average = np.sqrt(sum((salary - salary_average) ** 2) / len(salary))
variance0 = sqrt_average ** 2
variance1 = sqrt_average ** 2 * N / (N - 1)
print(f"среднее арифметическое = {salary_average:.1f},\n\
среднее квадратичное отклонение = {sqrt_average:.2f},\n\
смещенная дисперсия = {variance0:.3f},\n\
несмещенная дисперсия = {variance1:.3f}")

# среднее арифметическое = 65.3,
# среднее квадратичное отклонение = 30.82,
# смещенная дисперсия = 950.110,
# несмещенная дисперсия = 1000.116

# %%
# 2. В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

# 2 белых из 1ого ящика, 1 белый из 2ого
P1 = (combination(5, 2) / combination(8, 2)) *\
     (combination(5, 1) * combination(7, 3) / combination(12, 4))

# 1 белый из 1ого ящика, 2 белых из 2ого ящика
P2 = (combination(5, 1) * combination(3, 1) / combination(8, 2)) *\
     (combination(5, 2) * combination(7, 2) / combination(12, 4))

# 0 белых из 1ого ящика, 3 белых из 2ого ящика
P3 = (combination(3, 2) / combination(8, 2)) *\
     (combination(5, 3) * combination(7, 1) / combination(12, 4))

print(f"2. P = {P1 + P2 + P3 :.3f}")

# P = 0.369

# %%
# 3. На соревновании по биатлону один из трех спортсменов стреляет и
# попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9,
# для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел
# произведен: a). первым спортсменом б). вторым спортсменом
# в). третьим спортсменом.

p1 = 0.9  # 1ый выстрелил и попал
p2 = 0.8  # 2ой выстрелил и попал
p3 = 0.6  # 3ий выстрелил и попал
p = 1/3   # Вероятность, что стреляет 1ый (2ой, 3ий)
# p0 = 1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6
p0 = p * p1 + p * p2 + p * p3  # выстрел удачный 0.767
# по ф-ле Байеса:
print(f"3.\na). первым спортсменом = {p * p1 / p0:.3f}\n\
б). вторым спортсменом = {p * p2 / p0:.3f}\n\
в). третьим спортсменом = {p * p3 / p0:.3f}")

# a). первым спортсменом = 0.391
# б). вторым спортсменом = 0.348
# в). третьим спортсменом = 0.261

# %%

# 4. В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7,
# а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a). на факультете A б). на факультете B
# в). на факультете C?

pA = 0.8  # студент факультета A сдаст первую сессию
pB = 0.7  # студент факультета B сдаст первую сессию
pC = 0.9  # студент факультета C сдаст первую сессию
# тк кол-во студентов на факультетах A и B равны,
# и для факультета С кол-во студентов = A + B
# вероятность, что студент учится на каждом из факультетов
PA = 1/4
PB = 1/4
PC = 1/2
# Вероятность успешно сдать сессию 0.825
# 1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9
P = pA * PA + pB * PB + pC * PC
# По ф-ле Байеса
print(f"4. Студент учится\na). на факультете A = {pA * PA / P:.3f}\n\
б). на факультете B = {pB * PB / P:.3f}\n\
в). на факультете C = {pC * PC / P:.3f}")

# a). на факультете A = 0.242
# б). на факультете B = 0.212
# в). на факультете C = 0.545

# %%

# 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти
# из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь
# г). от одной до двух деталей?

p1 = 0.1
p2 = 0.2
p3 = 0.25
# только две детали: 1ая и 2ая сломалась, 3я нет +
# 2ая и 3я сломалась, 1ая нет,
P1 = (p1 * p2 * p3)
# 1я и 3я сломалась, 2ая нет
P2 = (p1 * p2 * (1 - p3)) +\
     (p2 * (1 - p1) * p3) +\
     (p3 * p1 * (1 - p2))
# хотя бы одна деталь = 1 - ни одна не сломалась
P3 = 1 - (1 - p1)*(1 - p2)*(1 - p3)
# от одной до двух деталей = 1 - ни одна не сломалась - все 3 сломались
P4 = P3 - P1
print("5. Какова вероятность того, что в первый месяц выйдут из строя")
print(f"а). все детали = {P1:.3f}")
print(f"б). только две детали = {P2:.3f}")
print(f"в). хотя бы одна деталь = {P3:.3f}")
print(f"г). от одной до двух деталей = {P4:.3f}")

# а). все детали = 0.005
# б). только две детали = 0.080
# в). хотя бы одна деталь = 0.460
# г). от одной до двух деталей = 0.455
