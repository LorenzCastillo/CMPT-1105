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

    speedInput = int(input("How fast is your car travelling (km/h)? "))
    distanceInput = float(input("How far are you travelling for your trip (in hours)? "))

    tripDuration = distanceInput / speedInput

    # Check to see if the speed is higher than the minimum speed limit
    if speedInput > SMALL_TICKET_SPEED:
        ticketsGiven = distanceInput // TICKET_INTERVAL

        if speedInput > LARGE_TICKET_SPEED:
            ticketCost = tripDuration * LARGE_TICKET_COST
        else:
            ticketCost = tripDuration * SMALL_TICKET_COST

    # Calculate the amount of gas they consume
    gasAmount = tripDuration * LITRES_PER_HOUR
    gasCost = gasAmount * GAS_COST

    if ticketsGiven > 0:
        print(distanceInput, "–", end=" ")
        print(format(tripDuration, ".2f"), "take", end=" ")
        print(format(gasAmount, ".2f"), "litres of gas, for a cost of $", end="")
        print(format(gasCost, ".2f"), "(no tickets)")

    else:
        print(distanceInput, "km -- ", tripDuration, ", take ", gasAmount, " litres of gas, for a cost of $", gasCost, "(+", ticketsGiven, " $", ticketCost, "ticket(s))", sep="")
        print(gasCost, " (+", ticketsGiven, " $", ticketCost, "ticket(s))", sep="")



if __name__ == "__main__":
    lab3_1()