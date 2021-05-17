import pyinputplus
import time, random

for mult in range(10):
    num1= random.randint(0,9)
    num2 = random.randint(0,9)

    product = num1*num2
    print(f'Cual es la respuesta al producto de {num1}*{num2}?')
    answer = int(input())
