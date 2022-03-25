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

def hoursToMinutes (hourExample):
    newTime=time.strptime(hourExample,'%H:%M')
    minutes = newTime[3]*60 + newTime[4]
    return minutes
