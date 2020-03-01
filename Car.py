import math
class Car:
    
    def __init__(self,distance : float ,v0 :float,an : float, ap: float, max_speed = None,color = None):
        self.__x0 = -distance
        self.__v0 = v0 / 3.6  #km/h to m/s
        self.__an = an
        self.__ap = ap
        self.__max_speed = None if max_speed == None else max_speed / 3.6  #km/h to m/s
        self.__color = color
    
    def x_coordinate(self, time, accelerated=True):
        acc = self.__ap if accelerated else -self.__an
        generated_velocity = acc * time + self.__v0
        if self.__max_speed == None or generated_velocity <= self.__max_speed:
            return self.__x0 + self.__v0 * time + acc * time * time / 2
        
        t0 = (self.__max_speed - self.__v0) / acc
        return self.__x0 + self.__v0 * t0 + acc * t0 * t0 / 2 + self.__max_speed * (time - t0)
    
    def velocity(self, time, accelerated=True):
        
        if not accelerated:
            t0 = self.__v0 / self.__an
            if time >= t0:
                return 0
            return self.__v0 - self.__an * time
        return self.__v0 + self.__ap * time
        
    def starting_point(self):
        return self.__x0
    
    def color(self):
        return self.__color
    
    
    def collision_time(self,car):
        
        a = (self.__ap - car.__ap) / 2
        b = self.__v0 - car.__v0
        c = self.__x0 - car.__x0

        if a == 0:
            if b == 0:
                return math.inf
            print("BC",b,c)            
            return -c/b
        
        d = (b**2 - 4*a*c) 
        if d < 0:
            return math.inf
        d = d ** (1/2)
        
        t = (-b - d) / ( 2 * a)
        if(t < 0):
            t == (-b + d) / (2 * a)
        if( t < 0):
            return math.inf
        return t
        
        
            
        
    
    
        
    
        