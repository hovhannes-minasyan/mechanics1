import numpy as np
import matplotlib.pyplot as plt
from Environment import Environment 

"""
User Input
"""

#n = int(input("Number of points: "))
#time = []
#force = []
#for i in range(n):
#    time.append( float(input("Time instant: ")))
#    force.append( float(input("Force instant: ")))
#
#force_points = np.array([time,force]).T
#masses = (float(input("Mass 1: ")),float(input("Mass 2: ")),float(input("Mass 3: ")))
#myus = (float(input("Myu 1: ")),float(input("Myu 2: ")),float(input("Myu 3: ")))
#
#x1,y1 = (float(input("X10: ")),float(input("Y10: ")))
#x2,y2 = (float(input("X20: ")),float(input("Y20: ")))
#x3,y3 = (float(input("X30: ")),float(input("Y30: ")))



"""
# The interesting points are the breaking points of the graph, or such where 
# the velocity reamins constant or the object is not moving (horizontal line)
# They are the points where the friction either changes direction or overwhelms
# the cummulative force acting on the mass  

"""



print ("Case 1")
masses = (7,5,3)
myus = (0.5,0.5,0.7)

force_points = np.array([
        [0,0],
        [0.1,100],
        [0.2,200],
        [0.3,0],
        [0.4,0],
        [0.5,-100 ],
        [0.6,-300],
        [0.7,-100],
        [2.3,300]
        ])

x1 = y1 = x2 = y2 = x3 = y3 = 0


env = Environment(masses,myus,force_points,(0,0),(0,0),(0,0))
#env.generatePoints()


"""
The force that affects on the M1 seems to be too small, and the friction to be high enough not to let objects move. 
M1 is also counteracted by the Reaction force of the rope on the pulley.
Then when it turns negative, still for 0.1 seconds, it does not move. Later M1 starts going to the for some short point of time.

At this stage you may see that M2's velocity (slope) decreases, but it spikes with strong positive force applied on the object. 
In this stage, M1 goes to right. M3 follows M1 and thus pulls the M2 to right. The friction applied on M2 allows it to pull M3 up, 
thereforce the entire system starts to move in positive coorinates (both x and y)
"""

masses = (7,5,10)
myus = (0.5,0.5,0.7)

force_points = np.array([
        [0,0],
        [0.1,100],
        [0.2,200],
        [0.3,0],
        [0.4,0],
        [0.5,-100 ],
        [0.6,-300],
        [0.7,-100],
        [2.3,300],
        [3,300]
        ])

x1 = y1 = x2 = y2 = x3 = y3 = 0


env = Environment(masses,myus,force_points,(0,0),(0,0),(0,0))
#env.generatePoints()


"""
The difference here with the prvious case is making M3 heavier more than 3x
It result in increase in gravity which pulls it down very fast.
As you can see M1 hasn't changed much. M2 started to move faster to right as now M3 not only pulls it via going to the right but also to down

The only suspicious point we can find is around 1.6s where M3 has a sharp edge. Thats when the overal force acting on M3 in horizontal direction = 0 (a1 = 0)
Therefore there is no friction on M3 at that point, and it continues until around 1.8s till then the graph is a straight line (V3 = -|const|)
In the end as F reaches its maxumim its effect comes closer to the previous case where it starts moving upwards 
"""


masses = (1,10,1)
myus = (0,1,0)

force_points = np.array([
        [0,0],
        [0.1,100],
        [0.2,200],
        [0.3,0],
        [0.4,0],
        [0.5,-100 ],
        [0.6,-300],
        [0.7,-100],
        [2.3,30],
        [3,300]
        ])

x1 = y1 = x2 = y2 = x3 = y3 = 0


env = Environment(masses,myus,force_points,(0,0),(0,0),(0,0))
env.generatePoints()

"""
In the case above we increase the mass and friction of M2 to the highest point which results in in staying in its position 
untill the force does not reach its maximum value like + or - 300. As the duration of -300 is short you can only notice a little spike in the coordinate near
0.6s Later after 2.7s where the force is at its top, its starts moving rightwards
Untill then M1 is moving to the left beacuse f the strong force of reaction from the rope and the negative F.
M3 is going down again due to its gravity
"""
