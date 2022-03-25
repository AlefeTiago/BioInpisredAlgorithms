"""
Primeiramente é necessário importar as bibliotecas auxiliares para a implementação
do código. Como vamos sortear diversos eventos, se faz necessário a existência da
bilioteca Random e Math,
"""

import random
import math
import sys
import time

flights={}
people = [('Lisbon', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Brussels', 'BRU'),
          ('London', 'LHR')  ]

destiny = 'FCO'

for fileReader in open("flights.txt"):
    origin, destiny, departureTime, arriveTime, price = fileReader.split(',')
    flights.setdefault((origin, destiny),[])
    flights[(origin, destiny)].append((departureTime, arriveTime, int(price)))
print(flights)

def flightCalendar(calendar):
    flightId = -1
    totalPrice = 0
    for i in range(len(calendar)//2):
        cityName,cityCode = people[i][0], people[i][1]
        flightId += 1
        departureFlight = flights[(cityCode, destiny)][calendar[flightId]]
        totalPrice += departureFlight[2]
        flightId += 1
        flightBack = flights[(destiny, cityCode)][calendar[flightId]]
        totalPrice += flightBack[2]

