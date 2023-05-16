from Objects import*

#Number 0
def Chaotic():
    Body1=Object(name="Body1",r=50,v=-5,mass=SolarSystem["Mass"][0]/2)
    Body2=Object(name="Body2",r=-70,v=10,mass=SolarSystem["Mass"][0]/3)
    Body3=Object(name="Body3",r=100,v=15,mass=SolarSystem["Mass"][0])

    TIMES=70000

    return [Body1,Body2,Body3],TIMES

#Number 1
def TLS_InfiniteShape():
    Sun1=Object(name="Star 1",r=50,mass=SolarSystem["Mass"][0],motion=False)
    Sun2=Object(name="Star 2",r=-50,mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][3],r=150,mass=SolarSystem["Mass"][3],v=26.04)

    TIMES=100000

    return [Sun1,Sun2,Earth],TIMES

#Number 2
def TLS_Ellipse():
    Sun1=Object(name="Star 1",r=50,mass=SolarSystem["Mass"][0],motion=False)
    Sun2=Object(name="Star 2",r=-50,mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][3],r=150,mass=SolarSystem["Mass"][3],v=47)

    TIMES=150000

    return [Sun1,Sun2,Earth],TIMES

#Number 3
def TLS_Pinwheel():
    Sun1=Object(name="Star 1",r=50,mass=SolarSystem["Mass"][0],motion=False)
    Sun2=Object(name="Star 2",r=-50,mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][3],r=250,mass=SolarSystem["Mass"][3],v=25)

    TIMES=600000

    return [Sun1,Sun2,Earth],TIMES

#Number 4
def TLS_Hyperbola():
    Sun1=Object(name="Star 1",r=50,mass=SolarSystem["Mass"][0],motion=False)
    Sun2=Object(name="Star 2",r=-50,mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][3],r=75,mass=SolarSystem["Mass"][3],v=64)

    TIMES=125000

    return [Sun1,Sun2,Earth],TIMES

#Number 5
def MoonOrbit():
    Sun=Object(name=SolarSystem["Name"][0],r=0,mass=SolarSystem["Mass"][0],v=0)
    Planet=Object(name="Planet",r=300,mass=SolarSystem["Mass"][5],v=21.026)
    Moon=Object(name=SolarSystem["Name"][9],r=305,mass=SolarSystem["Mass"][9],v=26.059)

    TIMES=455000

    return [Sun,Planet,Moon],TIMES

#Number 6
def SMJ_One():
    Sun=Object(name=SolarSystem["Name"][0],r=0,mass=SolarSystem["Mass"][0])
    Mercury=Object(name=SolarSystem["Name"][1],r=250,theta=-60,mass=SolarSystem["Mass"][1],v=23.033)
    Jupiter=Object(name=SolarSystem["Name"][5],r=270,mass=SolarSystem["Mass"][5],v=22.163)

    TIMES=100000
    
    return [Sun,Mercury,Jupiter],TIMES

#Number 7
def SMJ_OneLocked():
    Sun=Object(name=SolarSystem["Name"][0],r=0,mass=SolarSystem["Mass"][0],motion=False)
    Mercury=Object(name=SolarSystem["Name"][1],r=250,theta=-60,mass=SolarSystem["Mass"][1],v=23.033)
    Jupiter=Object(name=SolarSystem["Name"][5],r=270,mass=SolarSystem["Mass"][5],v=22.163)

    TIMES=100000
    
    return [Sun,Mercury,Jupiter],TIMES

#Number 8
def SMJ_Two():
    Sun=Object(name=SolarSystem["Name"][0],r=0,mass=SolarSystem["Mass"][0])
    Mercury=Object(name=SolarSystem["Name"][1],r=67,mass=SolarSystem["Mass"][1],v=50)
    Jupiter=Object(name=SolarSystem["Name"][5],r=120,mass=SolarSystem["Mass"][5],v=30)

    TIMES=150000

    return [Sun,Mercury,Jupiter],TIMES

#Number 9
def SMJ_TwoLocked():
    Sun=Object(name=SolarSystem["Name"][0],r=0,mass=SolarSystem["Mass"][0],motion=False)
    Mercury=Object(name=SolarSystem["Name"][1],r=67,mass=SolarSystem["Mass"][1],v=50)
    Jupiter=Object(name=SolarSystem["Name"][5],r=120,mass=SolarSystem["Mass"][5],v=30)

    TIMES=150000

    return [Sun,Mercury,Jupiter],TIMES

#Number 10
def LP_L1_One():
    v=29.725
    R=150
    r=139.996150
    V=v*r/R
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][5],r=150,v=29.725,mass=SolarSystem["Mass"][5])
    Satellite=Object(name="Satellite",r=r,v=V)

    TIMES=100000

    return [Sun,Earth,Satellite],TIMES

#Number 11
def LP_L1_Two():
    v=29.725
    R=150
    r=139.996149
    V=v*r/R
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][5],r=150,v=29.725,mass=SolarSystem["Mass"][5])
    Satellite=Object(name="Satellite",r=r,v=V)

    TIMES=100000

    return [Sun,Earth,Satellite],TIMES

#Number 12
def LP_L2_One():
    v=29.725
    R=150
    r=160.4697527
    V=v*r/R
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][5],r=150,v=29.725,mass=SolarSystem["Mass"][5])
    Satellite=Object(name="Satellite",r=r,v=V)

    TIMES=120000

    return [Sun,Earth,Satellite],TIMES

#Number 13
def LP_L2_Two():
    v=29.725
    R=150
    r=160.4697526
    V=v*r/R
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0],motion=False)
    Earth=Object(name=SolarSystem["Name"][5],r=150,v=29.725,mass=SolarSystem["Mass"][5])
    Satellite=Object(name="Satellite",r=r,v=V)

    TIMES=120000

    return [Sun,Earth,Satellite],TIMES

#Number 14
def LP_L3():
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0])
    Earth=Object(name=SolarSystem["Name"][3],r=150,v=29.725,mass=SolarSystem["Mass"][3])
    Satellite=Object(name="Satellite",r=150,theta=180,v=29.725)

    TIMES=100000

    return [Sun,Earth,Satellite],TIMES

#Number 15
def LP_L4():
    Sun=Object(name=SolarSystem["Name"][0],mass=SolarSystem["Mass"][0])
    Earth=Object(name=SolarSystem["Name"][3],r=150,v=29.725,mass=SolarSystem["Mass"][3])
    Satellite=Object(name="Satellite",r=150,theta=60,v=29.725)

    TIMES=100000

    return [Sun,Earth,Satellite],TIMES

#List of presets
PRESETS=[Chaotic,
        TLS_InfiniteShape,
        TLS_Ellipse,
        TLS_Pinwheel,
        TLS_Hyperbola,
        MoonOrbit,
        SMJ_One,
        SMJ_OneLocked,
        SMJ_Two,
        SMJ_TwoLocked,
        LP_L1_One,
        LP_L1_Two,
        LP_L2_One,
        LP_L2_Two,
        LP_L3,
        LP_L4]