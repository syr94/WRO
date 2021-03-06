# -*- coding: utf-8 -*-
"""WRO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qtUtsEme-RHdW3XDT17XKZP3meREnViS
"""

import math
lenght_d=100 # Расстояние между датчиками
data=[float(i) for i in input().split(", ")]
n = len(data)//2
r1,r2=[],[]
gamma=[]
X,Y=[],[]
for i in range(n):
  r1.append(data[i*2])
  r2.append(data[i*2+1])
for r_1,r_2 in zip(r1,r2):
  gamma.append(math.acos((lenght_d**2 + r_2**2 - r_1**2) / (2*lenght_d*r_2 )))

for i in range(n):
  X.append(round(r2[i]*math.sin(gamma[i]),1))
  Y.append(round(r2[i]*math.sin(1.5708-gamma[i]),1))


SX= sum(X)    # Ищем а и б линейной функции
SY= sum(Y)
SXX=sum([x*x for x in X])
SXY =sum([x*y for x,y in zip(X,Y)])

a = (n*SXY - SX*SY) / (n*SXX - SX*SX)
b = (SY - a*SX) / n

dlina = math.sqrt((X[n-1] - X[0])**2 + (Y[n-1] - Y[0])**2) # Характеристики на момент последнего замерения
U = dlina / 18 #Скорость в секундах
t_1 = dlina / U 

X_120 = 120                                          #Характеристики на точке соприкосновения с углом обзора камеры
Y_120 = round((a * X_120 + b),1)
dlina_120 = round((math.sqrt((X_120 - X[0])**2 + (Y_120 - Y[0])**2)),1)

t_k = round((dlina_120/U - t_1),1)
if (Y_120>=30) and (Y_120<=70):
  print(t_k)
else:
  print('no')