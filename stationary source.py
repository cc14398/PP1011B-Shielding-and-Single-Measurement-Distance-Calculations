import scipy as sp
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
from matplotlib import cm
import time

start=time.clock()
#Detector locations
sourcecount=10000
meanlifetime=0.5
D1posx=D1posy=0
D2posx=20
D2posy=0
D3posx=10
D3posy=15

"""
#Generate time of decay
decaytime=sp.random.exponential(scale=meanlifetime,size=100000)
n, bins, patches = plt.hist(decaytime, 100, alpha = 0.90)
plt.title("Gamma decay time")
plt.xlabel("time (ms)")
plt.ylabel("number of events")
plt.show()

#Generate direction of decay
phi=sp.random.uniform(low=-sp.pi,high=sp.pi,size=100000)
theta=sp.random.uniform(low=-sp.pi,high=sp.pi,size=100000)
"""
print("Source at x=10, y=7.5")
sourceposx=5
sourceposy=5
R1sq=sp.square(D1posx-sourceposx)+sp.square(D1posy-sourceposy)
R2sq=sp.square(D2posx-sourceposx)+sp.square(D2posy-sourceposy)
R3sq=sp.square(D3posx-sourceposx)+sp.square(D3posy-sourceposy)
D1count=sourcecount/(R1sq)
D2count=sourcecount/(R2sq)
D3count=sourcecount/(R3sq)
print("Detector Readings")
print(D1count)
print(D2count)
print(D3count)
print("Distance from each detector")
print(sp.sqrt(R1sq))
print(sp.sqrt(R2sq))
print(sp.sqrt(R3sq))

"""
print("\n Source at x=5, y=3")
sourceposx=5
sourceposy=3
R1sq=sp.square(D1posx-sourceposx)+sp.square(D1posy-sourceposy)
R2sq=sp.square(D2posx-sourceposx)+sp.square(D2posy-sourceposy)
R3sq=sp.square(D3posx-sourceposx)+sp.square(D3posy-sourceposy)
D1count=sourcecount/(R1sq)
D2count=sourcecount/(R2sq)
D3count=sourcecount/(R3sq)
print("Detector Readings")
print(D1count)
print(D2count)
print(D3count)
print("Distance from each detector")
print(sp.sqrt(R1sq))
print(sp.sqrt(R2sq))
print(sp.sqrt(R3sq))


print("\n Source at x=19, y=14")
sourceposx=19
sourceposy=14
R1sq=sp.square(D1posx-sourceposx)+sp.square(D1posy-sourceposy)
R2sq=sp.square(D2posx-sourceposx)+sp.square(D2posy-sourceposy)
R3sq=sp.square(D3posx-sourceposx)+sp.square(D3posy-sourceposy)
D1count=sourcecount/(R1sq)
D2count=sourcecount/(R2sq)
D3count=sourcecount/(R3sq)
print("Detector Readings")
print(D1count)
print(D2count)
print(D3count)
print("Distance from each detector")
print(sp.sqrt(R1sq))
print(sp.sqrt(R2sq))
print(sp.sqrt(R3sq))

print("\n Source at x=1, y=1")
sourceposx=1
sourceposy=1
R1sq=sp.square(D1posx-sourceposx)+sp.square(D1posy-sourceposy)
R2sq=sp.square(D2posx-sourceposx)+sp.square(D2posy-sourceposy)
R3sq=sp.square(D3posx-sourceposx)+sp.square(D3posy-sourceposy)
D1count=sourcecount/(R1sq)
D2count=sourcecount/(R2sq)
D3count=sourcecount/(R3sq)
print("Detector Readings")
print(D1count)
print(D2count)
print(D3count)
print("Distance from each detector")
print(sp.sqrt(R1sq))
print(sp.sqrt(R2sq))
print(sp.sqrt(R3sq))
"""

"""
n, bins, patches = plt.hist(D1csmear, 100, alpha=0.90)
plt.title("Count distribution for D1")
plt.xlabel("Number of counts")
plt.ylabel("Number of times observed")
plt.show()

n, bins, patches = plt.hist(D2csmear, 100, alpha=0.90)
plt.title("Count distribution for D2")
plt.xlabel("Number of counts")
plt.ylabel("Number of times observed")
plt.show()

n, bins, patches = plt.hist(D3csmear, 100, alpha=0.90)
plt.title("Count distribution for D3")
plt.xlabel("Number of counts")
plt.ylabel("Number of times observed")
plt.show()
"""

#Need to add in detector resolution
#Check Poisson distrubutions are correct
#Relocalise source from Poisson distributed count rates

ratio1=sp.zeros((10000,1))
ratio2=sp.zeros((10000,1))
ratio3=sp.zeros((10000,1))
R1=sp.zeros((10000,1))
R2=sp.zeros((10000,1))
R3=sp.zeros((10000,1))
D1det=sp.zeros((10000,1))
D2det=sp.zeros((10000,1))
D3det=sp.zeros((10000,1))
smear=sp.zeros((10000,2))

for n in range(10000):
    D1csmear=sp.random.poisson(1,int(D1count))
    D2csmear=sp.random.poisson(1,int(D2count))
    D3csmear=sp.random.poisson(1,int(D3count))
    
    count1=0
#smear count on detector 1
    while count1<int(D1count):
        D1det[n]+=D1csmear[count1]
        #print(D1det)
        count1+=1
#smear count on detector 2    
    count2=0

    while count2<int(D2count):
        D2det[n]+=D2csmear[count2]
        #print(D2det)
        count2+=1
#smear count on detector 3    
    count3=0

    while count3<int(D3count):
        D3det[n]+=D3csmear[count3]
        #print(D3det)
        count3+=1
#Calculate how percentage of counts each detector gets    
    ratio1[n]=D1det[n]/(D1det[n]+D2det[n]+D3det[n])
    ratio2[n]=D2det[n]/(D1det[n]+D2det[n]+D3det[n])
    ratio3[n]=D3det[n]/(D1det[n]+D2det[n]+D3det[n])
#Find distance between source and detector assuming source count known    
    R1[n]=sp.sqrt(sourcecount/D1det[n])
    R2[n]=sp.sqrt(sourcecount/D2det[n])
    R3[n]=sp.sqrt(sourcecount/D3det[n])
#Find smeared source position    
    smear[n,0]=sp.divide(sp.square(R1[n])-sp.square(R2[n])+sp.square(D2posx-D1posx),2*(D2posx-D1posx))
    smear[n,1]=sp.divide(sp.square(R1[n])-sp.square(R3[n])+sp.square(D3posx-D1posx)+sp.square(D3posy-D1posy),2*(D3posy-D1posy))-sp.divide((D3posx-D1posx)*smear[n,0],D3posy-D1posy)
    

    
print(ratio1[0], "\n", ratio1[1])
print(ratio1[0]+ratio2[0]+ratio3[0])
print(R1[0], "\n", R2[0], "\n", R3[0])
print(smear[0,0], "\n", smear[0,1])



smearhist=sp.histogram2d(smear[:,0],smear[:,1],100)

a=sp.linspace(0,20,100)
b=sp.linspace(0,15,100)
x,y=sp.meshgrid(a,b)

plt.figure()
plt.contourf(x,y,smearhist[0],100,cmap=cm.jet)
plt.colorbar()
plt.title("Smeared location of source")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()