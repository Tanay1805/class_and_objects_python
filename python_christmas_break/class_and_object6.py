class vehicle:
    seating_capacity=30
    default_fare=seating_capacity*100
    inpt=str(input('Press Book to confirm:'))
    if inpt == 'Book':
        seating_capacity-1
    print('₹',default_fare,"The fare of your normal vehicle")

class bus(vehicle):
    total_fare=1000
    final_amount = total_fare + 100
    print(final_amount,"The fare if you travel from bus")

class color(vehicle):
    color_of_the_vehicle=('White')
    print(color_of_the_vehicle,'is the color of the vehicle')
    

