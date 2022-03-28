import random
import math
import sys
import time


def flightCalendar(calendar, people, flights):
    flightId = -1
    totalPrice = 0
    for i in range(len(calendar)//2):
        cityName= people[i][0]
        origin= people[i][1]
        destiny = 'FCO'
        flightId += 1
        departureFlight = flights[(origin, destiny)][calendar[flightId]]
        totalPrice += departureFlight[2]
        flightId += 1
        flightBack = flights[(destiny, origin)][calendar[flightId]]
        totalPrice += flightBack[2]
        print('%10s%10s %5s-%5s U$%3s %5s-%5s U$%3s' % (cityName, origin, departureFlight[0], departureFlight[1], departureFlight[2],
                                                        flightBack[0], flightBack[1], flightBack[2]))
    print('Preço Total:', totalPrice)


def hoursToMinutes (hourExample):
    newTime=time.strptime(hourExample,'%H:%M')
    minutes = newTime[3]*60 + newTime[4]
    return minutes

def CostFunction (calendar, people, flights):
    destiny = 'FCO'

    totalPrice = 0
    lastArrive = 0
    firstExit = 1439

    flightId=-1

    for i in range (len(calendar)//2):
        origin = people[i][1]
        flightId+= 1
        flightGoing= flights[(origin, destiny)][calendar[flightId]]
        flightId+=1
        flightComing= flights[(destiny, origin)][calendar[flightId]]
        totalPrice+=flightGoing[2]
        totalPrice +=flightGoing[2]

        if lastArrive < hoursToMinutes(flightGoing[1]):
            lastArrive = hoursToMinutes(flightGoing[1])
        if firstExit > hoursToMinutes(flightComing[0]):
            firstExit = hoursToMinutes(flightComing[0])

    totalWait= 0
    flightId=-1

    for i in range(len(calendar) // 2):
        origin=people[i][1]
        flightId+=1
        flightGoing = flights[(origin, destiny)][calendar[flightId]]
        flightId += 1
        flightComing = flights[(destiny, origin)][calendar[flightId]]

        totalWait+=lastArrive - hoursToMinutes(flightGoing[1])
        totalWait += hoursToMinutes(flightComing[0]) - firstExit

    return (totalPrice + totalWait)

def Mutation(people, pace, calendar):
    domain = [(0,9)] * (len(people)*2)
    gene = random.randint(0, len(domain)-1)
    mutant = calendar
    if random.random() <0.05:
        if calendar[gene] != domain[gene][0]:
            mutant = calendar[0:gene] + [calendar[gene]-pace] + calendar[gene + 1:]
        else:
            if calendar[gene] != domain[gene][1]:
                mutant = calendar[0:gene] + [calendar[gene] + pace] + calendar[gene + 1:]
    return mutant

def CrossOver(people,chromossom1, chromossom2 ):
    domain = [(0, 9)] * (len(people) * 2)
    gene = random.randint(1, len(domain)-2)
    return chromossom1[0:gene] + chromossom2[gene:]

def GeneticAlgorithm(people,fitnessFunction, populationSize=100, pace=1, elitism=0.2, GenerationNumbers = 500):
    domain = [(0, 9)] * (len(people) * 2)
    population = []
    for i in range (populationSize):
        chromossom = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
        population.append(chromossom)
    numberElitism = int(elitism * populationSize)

    for i in range(GenerationNumbers):
        costs = [(fitnessFunction(chromossom), chromossom) for chromossom in population]
        costs.sort()
        sortedChromossoms = [chromossom for (cost, chromossom) in costs]
        population = sortedChromossoms[0: numberElitism]
        while  len(population) < populationSize:
            chromossom1=random.randint(0, numberElitism)
            chromossom2 = random.randint(0, numberElitism)
            newChromossom=CrossOver(domain, sortedChromossoms[chromossom1],sortedChromossoms[chromossom2])
            mutationNewChromossom = Mutation(domain, pace, newChromossom)
            population.append(mutationNewChromossom)

    return costs[0][1]