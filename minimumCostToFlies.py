"""
Primeiramente é necessário importar as bibliotecas auxiliares para a implementação
do código. Como vamos sortear diversos eventos, se faz necessário a existência da
bilioteca Random e Math,
"""

import random
import math
import sys
import time
from auxiliarFunctions import flightCalendar, hoursToMinutes, CostFunction

flights={}
people = [('Lisbon', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Brussels', 'BRU'),
          ('London', 'LHR')]

destiny = 'FCO'

for fileReader in open("flights.txt"):
    origin, destiny, departureTime, arriveTime, price = fileReader.split(',')
    flights.setdefault((origin, destiny),[])
    flights[(origin, destiny)].append((departureTime, arriveTime, int(price)))

"""
Testando as funcoes implementadas
"""
print(CostFunction([1,4, 3,1, 8,3, 6,3, 2,4, 5,3], people, flights))


