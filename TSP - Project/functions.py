import time
import tsp
from databaseExample import *


def hotelSelect(desCity):
    print('Average Hotel Cost in ', desCity, ' is : ',hotel[2][1])
    return int(hotel[2][1])

def transport(userInput):
    if userInput == 0: travel('Delhi','Mumbai')
    cost = 0
    if userInput == 1:
        print('Type of Train : \n1. General\n2. Sleeper\n3. AC\n4.Deluxe\n"{Sleeper for Now}"\n')
        ans = int(input())
        print('Selected Option :',ans)
        print('Calculating Details and cost')
        time.sleep(5)
        print('Distance will be : ',distanceMatrix[2][1],' KM')
        print('Train Name : ', 'Sample Train XYZ')
        print('Train Cost : INR ',trainEconomy[2][1])
        cost = int(trainEconomy[2][1])
    elif userInput == 2:
        print('Type of Flight : \n1. Economy\n2. Business\n"{Economy for Now}"\n')
        ans = int(input())
        print('Selected Option :',ans)
        print('Calculating Details and cost')
        time.sleep(5)
        print('Flight Name : ', 'Sample flight XYZ')
        print('Flight Cost : INR ',flightCost[2][1])
        cost = int(flightCost[2][1])
    elif userInput ==3:
        print('Calculating Details and cost')
        time.sleep(5)
        print('Bus Name : ', 'Sample Bus XYZ')
        print('Bus Cost : INR ',busCostAC[2][1])
        cost = int(busCostAC[2][1])
    return cost

def travel(city1, city2):
    print('Provide input 0 anytime to reset\n')
    print('Mode of Transport\n1. Train\n2. Flight\n3. Bus\n')
    userInput = int(input())
    transport(userInput)
    time.sleep(2)
    print('Looking for Hotel Price\n')
    hotelSelect(city2)
    print('Averaging City Travel Cost')
    time.sleep(2)
    print('Cheking CAB Rates')
    time.sleep(3)
    print('Cab rate is INR 50 for first 2 KM rest INR 30/KM')
    time.sleep(2)
    print('These are the Famous Destinations in Mumbai : \n')
    print(mumbaiDest)
    print('Applying TSP Algorithm\n')
    r = range(len(mumbai))
    dist = {(i, j): mumbai[i][j] for i in r for j in r}
    sol = tsp.tsp(r, dist)
    ans = ''
    for i in sol[1]:
        ans += mumbaiDest[str(i)]+' -> '
    time.sleep(2)
    print('This could be your path : \n')
    print(ans[:-2])
    time.sleep(3)
    print('Calculating your Total Cost now :\n')
    print('Total Cost in INR : ',1800+2700+3500)
    print('Script Ended')


