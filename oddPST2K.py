import numpy as np
import scipy as sp
import math
from matplotlib import pylab as plt
from ROOT import TTree, TFile, TH2D, TCanvas, TH1F, gROOT
from root_numpy import array2hist, hist2array, fill_hist, tree2array,root2array
from scipy.stats import gaussian_kde

input1="../../../storage/cc14398/Co60-10s-21Mar/PS50cm.root"
input2="../../../storage/cc14398/Co60-10s-21Mar/PS150cm.root"
input3="../../../storage/cc14398/Co60-10s-21Mar/PS250cm.root"
input4="../../../storage/cc14398/Co60-10s-21Mar/PS350cm.root"
input5="../../../storage/cc14398/Co60-10s-21Mar/PS450cm.root"
input6="../../../storage/cc14398/Co60-10s-21Mar/PS550cm.root"
#input7="../../../storage/cc14398/Co60-1s-15Mar/Co60-1s-PS7m.root"
#input8="../../../storage/cc14398/Co60-1s-15Mar/Co60-1s-PS8m.root"
#input9="../../../storage/cc14398/Co60-1s-15Mar/Co60-1s-PS9m.root"
#input10="../../../storage/cc14398/Co60-1s-15Mar/Co60-1s-PS10m.root"


KE1=root2array(input1,treename="PhaseSpace", branches="Ekine")
KE2=root2array(input2,treename="PhaseSpace",branches="Ekine")
KE3=root2array(input3,treename="PhaseSpace",branches="Ekine")
KE4=root2array(input4,treename="PhaseSpace",branches="Ekine")
KE5=root2array(input5,treename="PhaseSpace",branches="Ekine")
KE6=root2array(input6,treename="PhaseSpace",branches="Ekine")
#KE7=root2array(input6,treename="PhaseSpace",branches="Ekine")
#KE8=root2array(input6,treename="PhaseSpace",branches="Ekine")
#KE9=root2array(input6,treename="PhaseSpace",branches="Ekine")
#KE10=root2array(input6,treename="PhaseSpace",branches="Ekine")

print('Total entries')
print(KE1.size)
print(KE2.size)
print(KE3.size)
print(KE4.size)
print(KE5.size)
print(KE6.size)

print('Entries over 1MeV')
print(sum(i>1 for i in KE1))
print(sum(i>1 for i in KE2))
print(sum(i>1 for i in KE3))
print(sum(i>1 for i in KE4))
print(sum(i>1 for i in KE5))
print(sum(i>1 for i in KE6))
"""
print(KE7.size)
print(KE8.size)
print(KE9.size)
print(KE10.size)
"""

#dX=root2array(inputFile,treename="PhaseSpace", branches="dX")
"""
density1=gaussian_kde(KE1)
density2=gaussian_kde(KE2)
density3=gaussian_kde(KE3)
density4=gaussian_kde(KE4)
density5=gaussian_kde(KE5)
#density6=gaussian_kde(KE6)
"""

hist1, bin_edges1 = np.histogram(KE1, bins=20)
bin_c1= (bin_edges1[:-1] + bin_edges1[1:])/2
#plt.step(bin_c1,hist1)
plt.bar(bin_c1,hist1,width=np.diff(bin_edges1),color='none',edgecolor='b',label='1m')

hist2, bin_edges2 = np.histogram(KE2, bins=20)
bin_c2= (bin_edges2[:-1] + bin_edges2[1:])/2
#plt.step(bin_c2,hist2)
plt.bar(bin_c2,4*hist2,width=np.diff(bin_edges2),color='none',edgecolor='r',label='2m')

hist3, bin_edges3 = np.histogram(KE3, bins=20)
bin_c3= (bin_edges3[:-1] + bin_edges3[1:])/2
#plt.step(bin_c2,hist2)
plt.bar(bin_c3,9*hist3,width=np.diff(bin_edges3),color='none',edgecolor='c',label='3m')

hist4, bin_edges4 = np.histogram(KE4, bins=20)
bin_c4= (bin_edges4[:-1] + bin_edges4[1:])/2
#plt.step(bin_c2,hist2)
plt.bar(bin_c4,16*hist4,width=np.diff(bin_edges4),color='none',edgecolor='m',label='4m')

hist5, bin_edges5 = np.histogram(KE5, bins=20)
hist6, bin_edges6 = np.histogram(KE6, bins=20)

plt.xlabel('Kinetic Energy (MeV)',fontsize=16)
plt.ylabel('Count Rate x Distance \u00b2',fontsize=16 )


print('bins')
print(bin_edges1.size)
print(bin_edges2.size)
print(bin_edges3.size)
print(bin_edges4.size)
print(bin_edges5.size)
print(bin_edges6.size)

print('Areas Under 1MeV')
print(sum(np.diff(bin_edges1)[0:16]*hist1[0:16]))
print(sum(np.diff(bin_edges2)[0:16]*hist2[0:16]))
print(sum(np.diff(bin_edges3)[0:16]*hist3[0:16]))
print(sum(np.diff(bin_edges4)[0:16]*hist4[0:16]))
print(sum(np.diff(bin_edges5)[0:16]*hist5[0:16]))
print(sum(np.diff(bin_edges6)[0:16]*hist6[0:16]))

print('Total Area')
print(sum(np.diff(bin_edges1)*hist1))
print(sum(np.diff(bin_edges2)*hist2))
print(sum(np.diff(bin_edges3)*hist3))
print(sum(np.diff(bin_edges4)*hist4))
print(sum(np.diff(bin_edges5)*hist5))
print(sum(np.diff(bin_edges6)*hist6))

"""
plt.hist(KE1,bins=20,histtype='step',label='1m')
plt.hist(np.divide(KE2,4),bins=20,histtype='step',label='1m')
plt.hist(np.divide(KE3,9),bins=20,histtype='step',label='1m')
"""
#plt.hist2d(E_kinetic,dX)

"""
fig, ax1 = plt.subplots()
ax1.hist([KE1,KE2,KE3], label=['1m','3m','7m'],bins=15,density=True)

plt.hist(KE1,20,alpha=0.5,label='1m',range=[0,1.1],density=True)
plt.hist(KE2,20,alpha=0.5,label='4m',range=[0,1.1],density=True)
plt.hist(KE3,20,alpha=0.5,label='7m',range=[0,1.1],density=True)
"""

"""
xs=np.linspace(0,1.5,200)
density1.covariance_factor = lambda : .1
density1._compute_covariance()
plt.plot(xs,density1(xs),label='1m')
density2.covariance_factor = lambda : .1
density2._compute_covariance()
plt.plot(xs,density2(xs),label='2m')
density3.covariance_factor = lambda : .1
density3._compute_covariance()
plt.plot(xs,density3(xs),label='3m')
density4.covariance_factor = lambda : .1
density4._compute_covariance()
plt.plot(xs,density4(xs),label='4m')
density5.covariance_factor = lambda : .1
density5._compute_covariance()
plt.plot(xs,density5(xs),label='5m')
#density6.covariance_factor = lambda : .1
#density6._compute_covariance()
#plt.plot(xs,density6(xs),label='6m')
"""
plt.legend()
plt.pause(0.01)
input("press enter to exit")
