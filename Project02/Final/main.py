import numpy as np
import matplotlib.pyplot as plt
g = 10


#test_data
masses = (7,5,10)
myus = (0.5,0.5,0.7)

force_points = np.array([
        [0,0],
        [1,400],
        [2,400],
        [3,400],
        [4,3000],
        [5,0  ],
        [6,-100],
        [7,-2000]
        ])/10

x1 = y1 = x2 = y2 = x3 = y3 = 0

#end of test data



# Comment the section below to activate the test data
n = int(input("Number of points: "))
time = []
force = []
for i in range(n):
    time.append( float(input("Time instant: ")))
    force.append( float(input("Force instant: ")))

force_points = np.array([time,force]).T
masses = (float(input("Mass 1: ")),float(input("Mass 2: ")),float(input("Mass 3: ")))
myus = (float(input("Myu 1: ")),float(input("Myu 2: ")),float(input("Myu 3: ")))

x1,y1 = (float(input("X10: ")),float(input("Y10: ")))
x2,y2 = (float(input("X20: ")),float(input("Y20: ")))
x3,y3 = (float(input("X30: ")),float(input("Y30: ")))

# Uncomment the section above to disactivate the test data



def force_magnitude(t):
    
    for i in range(len(force_points)):
        if(t == force_points[i,0]):
            return force_points[i,1]
        if t > force_points[i,0]:
            continue
        
        x1,y1 = (force_points[i-1])
        x2,y2 = (force_points[i])
        m = (y2 - y1)/(x2 - x1)        
        return (t - x1)*m + y1
    
    return force_points[-1,1]


def acceleration_helper(myu1, myu2, myu3,F):
    M1,M2,M3 = masses
    
    Mat = np.array([
        [1, 0,  0,  -M3],
        [1, 0,  -M2,0],
        [myu1 + 1,M1,0,0],
        [0,1,-1,-1]
        ])
    
    b = np.array([
        M3*g - myu3*F,
        myu2*M2*g,
        F - myu1 * g * (M1 + M2),
        0
        ])
    
    return (np.linalg.inv(Mat) @ b)[1:]

def acceleration(t,vel):
    F = force_magnitude(t)
    myu1, myu2, myu3 = myus
    
        
    if(vel[2] > 0):
        myu3 *= -1
    if(vel[0] < 0):
        myu1 *= -1
    if(vel[1] < 0):
        myu2 *= -1
    
    
    M1,M2,M3 = masses
    
    Mat = np.array([
        [myu1 + 1,M1,0,0],
        [1, 0,  -M2,0],
        [1, 0,  0,  -M3],       
        [0,1,-1,-1]
        ])
    
    b = np.array([
        F - myu1 * g * (M1 + M2),        
        myu2*M2*g,
        M3*g - myu3*F,
        0
        ])
    
    acc = (np.linalg.inv(Mat) @ b)[-1:0:-1]
    
    new_acc = [None,None,None]
    if vel[1] == 0 and acc[0]**2 < (g*myu1)**2:
        new_acc[0] = 0
        Mat = np.delete(Mat, 0, 0)
        Mat = np.delete(Mat, 0, 1)
        b =np.delete(b, 1)  
    if vel[1] == 0 and acc[1]**2 < (g*myu2)**2:      
        new_acc[1] = 0
        if len(Mat) == 4:
            Mat = np.delete(Mat, 1, 0)
            Mat = np.delete(Mat, 1, 1)
            b =np.delete(b, 1)
        elif len(Mat) == 3:
            Mat = np.delete(Mat, 0, 0)
            Mat = np.delete(Mat, 0, 1)
            b =np.delete(b, 0)
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
            
    acc = (np.linalg.inv(Mat) @ b)[-1:0:-1]
    ind = 0
    for i in range(3):
        if new_acc[i] == None:
            new_acc[i] = acc[ind]
            ind += 1
                        
            
    return np.array(new_acc)


max_t = np.max(force_points[:,0])
delta_t = max_t / 1000
time_points = np.arange(0,max_t,delta_t)

velocity = np.array([[0,0,0]])
coordinate = np.array([[x1,x2,y3]])
for i in range(len(time_points)-1):
    t = time_points[i]
    acc = acceleration(t,velocity[i])    
    velocity = np.append(velocity, [velocity[i] + acc*delta_t],0)
    coordinate = np.append(coordinate,[acc*t*t/2 + velocity[i]*t + coordinate[i]],0)
n = len(coordinate)
x1,y1 = (coordinate[:,0],np.ones(n) * y1)
x2,y2 = (coordinate[:,1],np.ones(n) * y2)
x3,y3 = (x1,coordinate[:,2])


plt.xlabel("Time(s)")
plt.ylabel("X 1 (m)")
plt.plot(time_points,x1,color = "red")
plt.legend(["x1"])
plt.show()

plt.xlabel("Time(s)")
plt.ylabel("X 2 (m)")
plt.plot(time_points,x2,color = "green")
plt.legend(["x2"])
plt.show()

plt.xlabel("Time(s)")
plt.ylabel("Y 3 (m)")
plt.plot(time_points,y3, color= "blue")
plt.legend(["y3"])



# The interesting points are the breaking points of the graph, or such where 
# the velocity reamins constant or the object is not moving (horizontal line)
# They are the points where the friction either changes direction or overwhelms
# the cummulative force acting on the mass  


#


