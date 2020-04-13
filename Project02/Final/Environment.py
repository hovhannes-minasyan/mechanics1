import numpy as np
import matplotlib.pyplot as plt

class Environment:
    
    def __init__(self,masses,myus,force_points,c1,c2,c3,g=10,precision = 1000):
        self.precision = precision
        self.g = 10
        
        self.masses = masses
        self.myus = myus

        self.force_points = np.array(force_points)

        self.x1,self.y1 = c1
        self.x2,self.y2 = c2
        self.x3, self.y3 = c3
    
    def force_magnitude(self,t):
        for i in range(len(self.force_points)):
            if(t == self.force_points[i,0]):
                return self.force_points[i,1]
            if t > self.force_points[i,0]:
                continue
            
            p1,o1 = (self.force_points[i-1])
            p2,o2 = (self.force_points[i])
            m = (o2 - o1)/(p2 - p1)        
            return (t - p1)*m + o1
        
        return self.force_points[-1,1]


    
    
    def acceleration(self,t,vel,print_data = False):
        F = self.force_magnitude(t)
        myu1, myu2, myu3 = self.myus
        
            
        if(vel[2] > 0):
            myu3 *= -1
        if(vel[0] < 0):
            myu1 *= -1
        if(vel[1] < 0):
            myu2 *= -1
        
        
        M1,M2,M3 = self.masses
        
        Mat = np.array([
            [myu1 + 1,M1,0,0],
            [1, 0,  -M2,0],
            [1, M3*myu3,  0,  -M3],       
            [0,1,-1,-1]
            ])
        
        b = np.array([
            F - myu1 * self.g * (M1 + M2),        
            myu2*M2*self.g,
            M3*self.g,
            0
            ])
        
        acc = (np.linalg.inv(Mat) @ b)[1:]
        
        new_acc = [None,None,None]
        if vel[1] == 0 and acc[0]**2 < (self.g*myu1)**2:
            new_acc[0] = 0
            Mat = np.delete(Mat, 0, 0)
            Mat = np.delete(Mat, 0, 1)
            b =np.delete(b, 1)  
            
            #print("Activated 1")
            
        if vel[1] == 0 and acc[1]**2 < (self.g*myu2)**2:      
            new_acc[1] = 0
            if len(Mat) == 4:
                Mat = np.delete(Mat, 1, 0)
                Mat = np.delete(Mat, 1, 1)
                b =np.delete(b, 1)
            elif len(Mat) == 3:
                Mat = np.delete(Mat, 0, 0)
                Mat = np.delete(Mat, 0, 1)
                b =np.delete(b, 0)
                
            #print("Activated 2")
            
        if vel[2] == 0 and (acc[2]*M3)**2 < (F*myu3)**2:
            new_acc[2] = 0
            if len(Mat) == 4:
                Mat = np.delete(Mat, 2, 0)
                Mat = np.delete(Mat, 2, 1)
                b = np.delete(b, 2)
            elif len(Mat) == 3 :
                Mat = np.delete(Mat, 1, 0)
                Mat = np.delete(Mat, 1, 1)
                b = np.delete(b, 1)
            elif len(Mat) == 2 :
                Mat = np.delete(Mat, 0, 0)
                Mat = np.delete(Mat, 0, 1)
                b = np.delete(b, 0)
                
            #print("Activated 3")
        
        if(print_data):
            print(Mat)
            print(b)
            
        acc = (np.linalg.inv(Mat) @ b)[1:]
        ind = 0
        for i in range(3):
            if new_acc[i] == None:
                new_acc[i] = acc[ind]
                ind += 1
                            
                
        return np.array(new_acc)
    
    def generatePoints(self):
        max_t = np.max(self.force_points[:,0])
        delta_t = max_t / self.precision
        time_points = np.arange(0,max_t,delta_t)
        
        velocity = np.array([[0,0,0]])
        self.accelerations = []
        coordinate = np.array([[self.x1,self.x2,self.y3]])
        for i in range(len(time_points)-1):
            t = time_points[i]
            acc = self.acceleration(t,velocity[i])   
            self.accelerations.append(acc)
        
            
            velocity = np.append(velocity, [velocity[i] + acc*delta_t],0)
            coordinate = np.append(coordinate,[acc*t*t/2 + velocity[i]*t + coordinate[i]],0)
        n = len(coordinate)
        self.x1,self.y1 = (coordinate[:,0],np.ones(n) * self.y1)
        self.x2,self.y2 = (coordinate[:,1],np.ones(n) * self.y2)
        self.x3,self.y3 = (self.x1,coordinate[:,2])
        
        
        plt.xlabel("Time(s)")
        plt.ylabel("X 1 (m)")
        plt.plot(time_points,self.x1,color = "red")
        plt.legend(["x1"])
        plt.show()
        
        plt.xlabel("Time(s)")
        plt.ylabel("X 2 (m)")
        plt.plot(time_points,self.x2,color = "green")
        plt.legend(["x2"])
        plt.show()
        
        plt.xlabel("Time(s)")
        plt.ylabel("Y 3 (m)")
        plt.plot(time_points,self.y3, color= "blue")
        plt.legend(["y3"])
        plt.show()


