import matplotlib.pyplot as plt
from Car import Car

class Road:
    def __init__(self, ds : float ,dt:float):
        self.__dt = dt
        self.__ds = ds
        self.__cars = []
        self.__acc = []
        
        self.__count = 1000
        step = dt / self.__count
        self.__times = [0] * self.__count
        for i in range(1,self.__count):
            self.__times[i] = self.__times[i - 1] + step
            
    
    def add_car(self,car : Car):
        self.__cars.append(car)
        self.__cars = sorted(self.__cars,key=lambda i:i.starting_point(),reverse=True)
    
    def plot(self):
        plt.axhspan(0, self.__ds, color='y', alpha=0.5, lw=0)
        
        plt.axhline(y=0, color='r', linestyle='-',linewidth=0.5)
        plt.axhline(y=self.__ds, color='r', linestyle='-',linewidth=0.5)
        #plt.axvline(x=0, color='r', linestyle='-',linewidth=0.5)
        plt.axvline(x=self.__dt, color='r', linestyle='-',linewidth=0.5)
        plt.ylabel("X-Coordinate")
        plt.xlabel("Time")
        
        for j in range(len(self.__cars)):
            car = self.__cars[j]
            coords = [car.x_coordinate(i,not self.__acc[j]) for i in self.__times] 
            plt.plot(self.__times, coords, color = car.color())        
        
        plt.show()
        
        
        plt.ylabel("Velocity")
        plt.xlabel("Time")
        
        for j in range(len(self.__cars)):
            car = self.__cars[j]
            vels = [car.velocity(i,not self.__acc[j]) for i in self.__times]
            #print (vels)
            plt.plot(self.__times, vels, color = car.color())        
        plt.show()
        
    def test_for_stop(self):  
        
        if len(self.__cars) == 0:
            return        
        
        last_decision = self.test_car_for_stop(self.__cars[0])
        self.__acc.append(last_decision)
        if last_decision :
            print("Car","1","Stop")
        else:
            print("Car","1","Go")

        for i in range(1,len(self.__cars)):
            if last_decision:
                self.__acc.append(last_decision)
                print("Car",str(i+1),"Stop")
                continue
            last_decision = self.test_car_for_stop(self.__cars[i],self.__cars[i-1])
            if last_decision :
                print("Car",str(i+1),"Stop")
            else:
                print("Car",str(i+1),"Go")
            self.__acc.append(last_decision)
        
        
    def test_car_for_stop(self,car : Car,front_car :Car = None):
        if front_car == None:
            coord = car.x_coordinate(self.__dt)
            return coord < self.__ds
        
        coord = car.x_coordinate(self.__dt)
        if coord < self.__ds:
            return True
      
        diff = [(front_car.x_coordinate(i) - car.x_coordinate(i)) < 0 for i in self.__times]
        return sum(diff) > 0
        
        #t = front_car.collision_time(car)
        
        if t < self.__dt:
            return True
        else:
            return False
    

        
        
        
            
        