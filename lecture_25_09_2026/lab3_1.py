def textDivider():
    print("------------")

def lab3_1():
    SMALL_TICKET_SPEED = 105
    LARGE_TICKET_SPEED = 125

    SMALL_TICKET_COST = 300
    LARGE_TICKET_COST = 500

    TICKET_INTERVAL = 3

    LITRES_PER_HOUR = 15
    GAS_COST = 3.50

    ticketsGiven = 0
    ticketCost = 0

    while True:
        try:
            speedInput = int(input("How fast is your car travelling (km/h)? "))
            if speedInput <= 0:
                print("Error: Please enter a value higher than 0")
                continue
            elif speedInput >= 500:
                print("I'm not a car guy... But the fastest a car can realistically go is 499km/h (from the Koenigsegg Jesko Absolut)")
                print("Error: Please enter a value lower than 500")
                continue
            else:
                break
        except ValueError:
            print("Error: Please enter an integer")

        textDivider()

    while True:
        try:
            distanceInput = float(input("How far are you travelling for your trip (in hours)? "))
            if distanceInput <= 0:
                print("Error: Please enter a value higher than 0")
                continue
            elif distanceInput >= 7500:
                print("That's like the drive from one side of Canada to the other...")
                print("Error: Please enter a value lower than 7500")
                continue
            else:
                break
        except ValueError:
            print("Error: Please enter an integer or float value")

        textDivider()


    tripDuration = distanceInput / speedInput

    # Check to see if the speed is higher than the minimum speed limit
    if speedInput > SMALL_TICKET_SPEED:
        ticketsGiven = tripDuration // TICKET_INTERVAL

        if speedInput > LARGE_TICKET_SPEED:
            ticketCost = ticketsGiven * LARGE_TICKET_COST
        else:
            ticketCost = ticketsGiven * SMALL_TICKET_COST

    # Calculate the amount of gas they consume
    gasAmount = LITRES_PER_HOUR * tripDuration
    gasCost = gasAmount * GAS_COST

    print("With", distanceInput, "km of travel in",
          format(tripDuration, ".2f"), "hours, you would need",
          format(gasAmount, ".2f"), "litres of gas, for a cost of $", end="")

    if ticketsGiven < 0:
        print(format(gasCost, ".2f"), "(no tickets)")

    else:
        print(format(gasCost, ".2f"), " (+ $",
              format(ticketCost, ".2f"), " for accumulating ",
              format(ticketsGiven, ".0f"), " ticket(s))", sep="")

if __name__ == "__main__":
    lab3_1()