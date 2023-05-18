from Presets import*

from matplotlib import pyplot as plt

def PlotTraejctory(OBJECTS,years):
    for object in OBJECTS:
        plt.scatter(object.x,object.y,label=object.name)
        plt.plot(object.xList,object.yList)

    plt.title("Three body problem - Years = "+str(years))
    plt.xlabel("x-position [10e9 m]")
    plt.ylabel("y-position [10e9 m]")
    plt.axis('scaled')
    plt.legend(loc="upper right")
    plt.show()

def PlotDistance(OBJECTS,DISTANCE,TIMES):
    
    time=np.arange(TIMES)

    for i in range(3):
        plt.plot(time,DISTANCE[i],label=OBJECTS[i].name+"-"+OBJECTS[(i+1)%3].name+" distance")

    plt.title("Distances between bodies")
    plt.xlabel("Number of time-steps")
    plt.ylabel("Distance [10e9 m]")
    plt.legend()
    plt.show()

def PlotEnergy(OBJECTS,TIMES):

    KineticEnergy=np.zeros(TIMES)
    PotentialEnergy=np.zeros(TIMES)

    for object in OBJECTS:
        #Sum of kinetic energies
        KineticEnergy+=np.array(object.KineticList)
        #Half the sum of potential energies
        PotentialEnergy+=0.5*np.array(object.PotentialList)

    TotalEnergy=KineticEnergy+PotentialEnergy
    time=np.arange(TIMES)

    plt.plot(time,KineticEnergy,c="r",label="Kinetic Energy")
    plt.plot(time,PotentialEnergy,c="b",label="Potential Energy")
    plt.plot(time,TotalEnergy,c="g",label="Total Energy")
    plt.title("Energy of the system")
    plt.xlabel("Number of time-steps")
    plt.ylabel("Energy [J]")
    plt.legend()
    plt.show()

def Plot(OBJECTS,DISTANCE,TIMES,years):

    PlotTraejctory(OBJECTS,years)
    PlotDistance(OBJECTS,DISTANCE,TIMES)
    PlotEnergy(OBJECTS,TIMES)
