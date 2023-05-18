from Settings import*

import numpy as np

class Object():
    def __init__(self,name="Object",mass=0,r=0,v=0,theta=0,phi=90,motion=True):
        
        self.name=name
        self.mass=mass

        #False=The object is locked
        self.motion=motion

        #x-y position
        self.x=r*np.cos(theta*np.pi/180)            
        self.y=r*np.sin(theta*np.pi/180)

        #Velocity components
        self.vx=v*np.cos((phi+theta)*np.pi/180)
        self.vy=v*np.sin((phi+theta)*np.pi/180)

        #Acceleration components
        self.ax=0
        self.ay=0

        #Trajectory
        self.xList=[self.x]
        self.yList=[self.y]

        #Energy
        self.KineticList=[]
        self.PotentialList=[]
        
    def FindDistances(self,Object1,Object2):
        x1=Object1.x-self.x
        y1=Object1.y-self.y
        x2=Object2.x-self.x
        y2=Object2.y-self.y

        #Distance with Object1
        d1=np.sqrt(x1**2+y1**2)
        #Distance with Object2
        d2=np.sqrt(x2**2+y2**2)
    
        return x1,x2,y1,y2,d1,d2

    def FindForces(self,Object1,Object2):

        x1,x2,y1,y2,d1,d2=self.FindDistances(Object1,Object2)

        #Acceleration components
        self.ax=G*((Object1.mass*x1)/(d1**3)+(Object2.mass*x2)/(d2**3))
        self.ay=G*((Object1.mass*y1)/(d1**3)+(Object2.mass*y2)/(d2**3))

        return d1,d2 

    def FindTau(self,Object1,Object2):

        d1,d2=self.FindForces(Object1,Object2)

        #Acceleration and speed
        a=np.sqrt(self.ax**2+self.ay**2)
        v=np.sqrt(self.vx**2+self.vy**2)

        #From quadratic equation formula
        new_TAU=(-v+np.sqrt(v**2+2*a*min(d1,d2)/CONST))/a

        return new_TAU
    
    def Energy(self,Object1,Object2):

        x1,x2,y1,y2,d1,d2=self.FindDistances(Object1,Object2)

        #Save energies
        self.KineticList.append(0.5*self.mass*(self.vx**2+self.vy**2)*10**21)
        self.PotentialList.append(-G*self.mass*(Object1.mass/d1+Object2.mass/d2)*10**21)

    def VerletPosition(self,new_TAU):

        #New position
        self.x+=self.vx*new_TAU+0.5*self.ax*new_TAU**2
        self.y+=self.vy*new_TAU+0.5*self.ay*new_TAU**2

        #Save position
        self.xList.append(self.x)
        self.yList.append(self.y)

    def VerletVelocity(self,Object1,Object2,new_TAU):
        
        #Save old acceleration
        old_ax=self.ax
        old_ay=self.ay

        d1,d2=self.FindForces(Object1,Object2)

        #New velocity
        self.vx+=0.5*new_TAU*(self.ax+old_ax) 
        self.vy+=0.5*new_TAU*(self.ay+old_ay) 
