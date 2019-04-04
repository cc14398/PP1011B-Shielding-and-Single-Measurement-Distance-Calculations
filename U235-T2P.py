import numpy as np
import scipy as sp
import math
from matplotlib import pylab as plt
from ROOT import TTree, TFile, TH2D, TCanvas, TH1F, gROOT
from root_numpy import array2hist, hist2array, fill_hist, tree2array,root2array

input1="../../../storage/cc14398/U235-10s-3Apr/PS50cm.root"
input2="../../../storage/cc14398/U235-10s-3Apr/PS150cm.root"
input3="../../../storage/cc14398/U235-10s-3Apr/PS250cm.root"
input4="../../../storage/cc14398/U235-10s-3Apr/PS350cm.root"
input5="../../../storage/cc14398/U235-10s-3Apr/PS450cm.root"
input6="../../../storage/cc14398/U235-10s-3Apr/PS550cm.root"
"""
input1="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm1.root"
input2="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm2.root"
input3="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm3.root"
input4="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm4.root"
input5="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm5.root"
input6="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm6.root"
input7="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm7.root"
input8="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm8.root"
input9="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm9.root"
input10="../../../hdfs/user/cc14398/U235-10s-1Apr/PS550cm10.root"
"""
KE1=root2array(input1,treename="PhaseSpace", branches="Ekine")
KE2=root2array(input2,treename="PhaseSpace",branches="Ekine")
KE3=root2array(input3,treename="PhaseSpace",branches="Ekine")
KE4=root2array(input4,treename="PhaseSpace",branches="Ekine")
KE5=root2array(input5,treename="PhaseSpace",branches="Ekine")
KE6=root2array(input6,treename="PhaseSpace",branches="Ekine")
"""
KE7=root2array(input7,treename="PhaseSpace",branches="Ekine")
KE8=root2array(input8,treename="PhaseSpace",branches="Ekine")
KE9=root2array(input9,treename="PhaseSpace",branches="Ekine")
KE10=root2array(input10,treename="PhaseSpace",branches="Ekine")
"""
print(KE1.size)
print(KE2.size)
print(KE3.size)
print(KE4.size)
print(KE5.size)
print(KE6.size)
"""
print(KE7.size)
print(KE8.size)
print(KE9.size)
print(KE10.size)
"""
print('Counts over 0.15MeV')
print(sum(i>0.15 for i in KE1))
print(sum(i>0.15 for i in KE2))
print(sum(i>0.15 for i in KE3))
print(sum(i>0.15 for i in KE4))
print(sum(i>0.15 for i in KE5))
print(sum(i>0.15 for i in KE6))
"""
print(sum(i>0.15 for i in KE7))
print(sum(i>0.15 for i in KE8))
print(sum(i>0.15 for i in KE9))
print(sum(i>0.15 for i in KE10))
"""
#dX=root2array(inputFile,treename="PhaseSpace", branches="dX")

plt.hist(KE1,bins=40,histtype='step',label='1m')
plt.hist(KE2,bins=40,histtype='step',label='2m')
plt.hist(KE3,bins=40,histtype='step',label='3m')
#plt.hist2d(E_kinetic,dX)

plt.xlabel('Kinetic Energy (MeV)')
plt.ylabel('Counts')

#fig, ax1 = plt.subplots()
#ax1.hist([KE1,KE2,KE3], label=['1m','3m','7m'],bins=15,density=True)

#plt.hist(KE1,20,alpha=0.5,label='1m',range=[0,1.1],density=True)
#plt.hist(KE2,20,alpha=0.5,label='4m',range=[0,1.1],density=True)
#plt.hist(KE3,20,alpha=0.5,label='7m',range=[0,1.1],density=True)

plt.legend(loc=1)
plt.pause(0.01)
input("press enter to exit")
