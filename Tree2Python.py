import numpy as np
import math
from matplotlib import pylab as plt
from ROOT import TTree, TFile, TH2D, TCanvas, TH1F, gROOT
from root_numpy import array2hist, hist2array, fill_hist, tree2array,root2array

input1="PS1m.root"
input2="PS2m.root"
input3="PS3m.root"
input4="PS4m.root"
KE1=root2array(input1,treename="PhaseSpace", branches="Ekine")
KE2=root2array(input2,treename="PhaseSpace",branches="Ekine")
KE3=root2array(input3,treename="PhaseSpace",branches="Ekine")
KE4=root2array(input4,treename="PhaseSpace",branches="Ekine")

#dX=root2array(inputFile,treename="PhaseSpace", branches="dX")

#plt.hist(E_kinetic,bins=20)
#plt.hist2d(E_kinetic,dX)
#plt.legend()

fig, ax1 = plt.subplots()
ax1.hist([KE1,KE2,KE3,KE4], label=['1m','2m','3m','4m'])
#plt.legend(bbox_to_anchor=(1,1))
plt.legend()
plt.pause(0.01)
input("press enter to exit")
