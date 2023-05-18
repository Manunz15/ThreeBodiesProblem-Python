from Plot import*

import time

def main():

    start_time=time.time()

    #Initializing
    OBJECTS,TIMES=PRESETS[5]()
    DISTANCE=np.zeros([3,TIMES])
    years=0     

    for j in range(TIMES):
        
        #Find the tau
        TAU_LIST=[TAU]
        for i in range(3):
            if OBJECTS[i].motion:
                TAU_LIST.append(OBJECTS[i].FindTau(OBJECTS[(i+1)%3],OBJECTS[(i+2)%3]))
        #Choose the smallest one
        new_TAU=min(TAU_LIST)
        
        #Count time
        years+=new_TAU

        #Calculate new position
        for i in range(3):
            OBJECTS[i].Energy(OBJECTS[(i+1)%3],OBJECTS[(i+2)%3])
            if OBJECTS[i].motion:
                OBJECTS[i].VerletPosition(new_TAU)

        #Calculate new Velocity
        for i in range(3):
            DISTANCE[i][j]=np.sqrt(
                (OBJECTS[i].x-OBJECTS[(i+1)%3].x)**2+
                (OBJECTS[i].y-OBJECTS[(i+1)%3].y)**2)
            if OBJECTS[i].motion:
                OBJECTS[i].VerletVelocity(OBJECTS[(i+1)%3],OBJECTS[(i+2)%3],new_TAU)
    
    #Convert time in years
    years=round((years*10**6)/(365*24*60*60),2)

    #Processing time
    end_time=time.time()
    print("Time =",end_time-start_time)

    #Plot data
    Plot(OBJECTS,DISTANCE,TIMES,years)

if __name__=="__main__":
    main()
