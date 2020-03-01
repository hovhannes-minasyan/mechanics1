from Car import Car
from Road import Road



def play():
    n = int(input("Number of cars: "))
    ds = float(input("Crossroad length: "))
    dt = float(input("Yellow light time: "))
    
    road = Road(ds,dt)
    
    prev = 0
    for i in range(n):
        x0 = 0
        v = float(input("Initial velocity: "))
        maxv = float(input("Maximum velocity: "))
        ap = float(input("Positive acceleration: "))
        an = float(input("Negative acceleration: "))
        if i == 0:
            x0 = prev + float(input("Initial distance: "))
        else:
            x0 = prev + float(input("Distance: from previous car"))
        prev = x0
        color = input("Color of the car: ")
        road.add_car(Car(x0,v,an,ap,maxv,color))
    
    road.test_for_stop()
    road.plot()
    

def test():
    car1 = Car(30,50,3,3,100,"blue")
    car2 = Car(20,80,3,3,100,"green")
    road = Road(1,2)
    road.add_car(car1)
    road.add_car(car2)
    road.test_for_stop()  
    road.plot()
    
    car1 = Car(30,40,1.5,2.5,100,"blue")
    road = Road(1,2)    
    road.add_car(car1)    
    road.test_for_stop()      
    road.plot()

play()
#test()


# =============================================================================
# The reports show that the increase in initial velocity and positive acceleration
# allow the car to pass the yellow light. If the car is also a lot further than
# the line, then even the limits of velocity and acceleration may not help.
# However, acceleration affects quadratically, so increase in acceleration with
# the same magnitude gives better chance of passing the yellow light than increase
# in the velocity with the same amount.

# =============================================================================

    

