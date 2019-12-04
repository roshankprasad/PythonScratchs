    #hackerrank seating Arrangment question
testcases = int(input())
for _ in range(0,testcases):
    seatNum = int(input())
    divby3 = int(seatNum / 3)
    modby3 = (seatNum % 3)
    seatBerth = ''
    if modby3 > 0:
        compartment = divby3 + 1
    else:
        compartment = divby3
    oppositeCompartment = 0
    if compartment % 4 == 1:
        oppositeCompartment = compartment + 3
    elif compartment % 4 == 2:
        oppositeCompartment = compartment + 1
    elif compartment % 4 == 3:
        oppositeCompartment = compartment - 1
    elif compartment % 4 == 0:
        oppositeCompartment = compartment - 3

    num = (compartment - 1) * 3
    oppositeSeat = oppositeCompartment * 3 - (seatNum - num) + 1

    if oppositeSeat % 2 != 0:
        if modby3 == 1:
            seatBerth = 'AS'
        elif modby3 == 2:
            seatBerth = 'MS'
        elif modby3 == 0:
            seatBerth = 'WS'
    else:
        if modby3 == 1:
            seatBerth = 'WS'
        elif modby3 == 2:
            seatBerth = 'MS'
        elif modby3 == 0:
            seatBerth = 'AS'

    print(oppositeSeat, seatBerth)