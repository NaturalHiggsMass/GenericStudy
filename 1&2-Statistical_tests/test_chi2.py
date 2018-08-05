import numpy as np 
import matplotlib.pyplot as plt

##khi2

mt=100
nb=1000
Npoints=101

#liste = np.random.poisson(mt, nb) 
liste = l
diff = np.linspace(-0.05*mt,0.05*mt,Npoints)

listeNest=np.zeros(len(diff))
listechi2_Nest=np.zeros(len(diff))
listechi2_moy=np.zeros(len(diff))
listechi2_Ni=np.zeros(len(diff))

moy = np.sum(liste) /nb 
print (moy)

for i in range (len(diff)):
    listeNest[i] = moy + diff[i]
    chi = np.zeros(nb)
    chi_moy = np.zeros(nb)
    chi_Ni = np.zeros(nb)
    for j in range (nb):
        chi[j] = ((liste[j] - listeNest[i])**2) / listeNest[i]
        chi_moy[j]= ((liste[j] - listeNest[i])**2) / mt
        if liste[j] == 0 :
            chi_Ni[j]=0
        else :
            chi_Ni[j]=((liste[j] - listeNest[i])**2) / liste[j] 
    listechi2_Nest[i] = np.sum (chi)
    listechi2_moy[i] = np.sum (chi_moy)
    listechi2_Ni[i] = np.sum (chi_Ni)


plt.plot(listeNest,listechi2_Nest-955.2423983039882,'b')
plt.plot(moy,listechi2_Nest[Npoints//2] - 955.2423983039882,'ro')
axes = plt.gca()
axes.xaxis.set_ticks(np.linspace(95,105,21))
for tickLabel in plt.gca().xaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
plt.ylim(-1,4)
plt.xlim(0.99*listeNest[Npoints//2 +5],1.011*listeNest[Npoints//2 +5])
plt.grid()
#plt.plot(listeNest,listechi2_moy, 'b--') 
#plt.plot(listeNest,listechi2_Ni, 'b--')
plt.show()

##likelihood

mu=100
nb=1000
Npoints=101

#liste = np.random.poisson(mu, nb) 
liste = l
diff = np.linspace(-0.05*mu,0.05*mu,Npoints)

listeNest=np.zeros(len(diff))
listelogL_Nest=np.zeros(len(diff))

moy = np.sum(liste) /nb 
print (moy)

for i in range (len(diff)):
    
    listeNest[i] = moy + diff[i]
    
    logLi = np.zeros(nb)
    for j in range (nb):
        logLi[j] = -listeNest[i] + liste[j]*np.log(listeNest[i]) - np.log(fact(liste[j]))
    listelogL_Nest[i] = np.sum (logLi)

plt.plot(listeNest,-2*listelogL_Nest+2*listelogL_Nest[Npoints//2],'b',moy, 0,'ro')
for tickLabel in plt.gca().xaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
axes = plt.gca()
axes.xaxis.set_ticks(np.linspace(90,120,61))
plt.plot(listeNest,[1]*101,'r--')
plt.grid()
plt.ylim(-1,4)
plt.xlim(0.99*moy,1.011*moy)
plt.show()

##factorielle
def fact(x):
    res=1
    for l in range (1,x+1):
        res = res * l
    return (float(res))
    
## liste de l'image finale

l = np.array([105, 104,  98, 107,  99,  98, 101,  80, 101,  95, 100, 108, 100,
       101,  86,  86,  84, 107,  98,  95, 105,  88,  81, 108, 107,  96,
       112,  90,  89, 110, 104, 103, 104, 108, 114,  99,  98,  70,  93,
        89,  94, 105, 104, 105, 101, 108, 104, 113, 100,  99, 109,  95,
        89, 102,  91,  84,  89,  95,  94, 105,  86, 116,  95, 110, 122,
       118, 106,  94, 111,  81,  93, 101, 100, 112, 112, 102,  93,  91,
       101, 102, 102, 105,  99,  99, 103, 103,  95, 112, 114,  95, 105,
       121,  98, 106,  97,  90, 103,  93,  94,  92,  97,  99, 105,  98,
       105, 105,  96, 108, 106, 111, 116, 118,  98, 105,  98,  97, 114,
        89,  87,  93, 112, 108, 105,  99, 103, 113, 103, 105,  84, 106,
        96, 107,  99,  95, 100, 112,  92, 123,  88, 100,  92, 104, 104,
       106,  93, 113, 110, 105, 103,  98, 106, 109,  93, 111,  94,  91,
       115, 103, 106, 112,  91, 101,  92,  97, 104, 107, 102,  91, 114,
        93, 114, 106,  92,  96, 111, 107,  94,  85, 104, 105, 105,  96,
       102,  78,  97, 105,  80, 111, 101,  89,  96, 116,  99, 102,  95,
        87, 128, 104, 107,  96, 101,  93,  82, 102,  95,  89,  87,  83,
       112,  93,  88, 114,  85, 102,  94, 114,  95,  85, 102,  85, 106,
       113,  95, 109, 105, 108,  97, 104,  94,  95, 111, 109,  98,  80,
        99,  98, 114, 119, 119, 101, 105,  98, 106,  88,  97, 102,  93,
        99, 113,  97, 121, 107,  88,  91,  90, 118, 100, 111,  98,  93,
        98, 105, 108, 107,  82,  80, 113,  93,  86,  89,  98, 106, 102,
       104, 112,  98,  81,  99, 114,  99,  82, 105,  95, 102,  88, 102,
        91,  99, 109, 104, 109, 124,  95,  95, 105, 136, 111, 100,  91,
       107, 102,  92, 113, 101,  93, 128, 110,  88,  98,  93,  92, 121,
       113,  97, 125,  92,  84,  83, 122, 113,  97, 104, 112,  93,  98,
        98,  94, 109,  98,  85, 121,  77, 104, 114,  87,  92, 111,  76,
       107,  97,  94, 101, 115,  81,  93, 101,  97, 107, 106, 112,  94,
        99,  96,  98,  92,  86, 114, 101, 115,  90,  84, 115,  87,  98,
       114, 116, 114, 111,  90,  97, 107, 113, 111,  82,  98,  85,  83,
        97, 109, 109, 108,  96,  98, 101, 101,  86, 107,  97, 103, 114,
       108, 101, 101,  79,  88, 107,  97, 116, 111,  87, 126, 101, 123,
        97, 107, 102,  91,  91, 111,  90, 122, 102, 108, 102, 104,  99,
        85, 104,  99, 119, 111, 119,  92, 100, 114, 103, 114,  93,  89,
       110, 112, 109,  89, 100, 126,  89, 100, 111,  90,  96, 111, 101,
       101,  94,  99, 108, 100, 104,  98, 109, 116, 112,  97, 109,  94,
       110, 105,  89, 105, 102, 107, 112,  91, 101, 118,  94,  89, 103,
       115, 106, 103,  96,  95,  97,  91, 108,  93,  92,  97,  93, 105,
        92,  93,  96, 109, 104, 103,  90,  95, 103, 108, 123, 103,  91,
        92,  82,  95, 103,  94, 100,  98, 105,  95,  94, 106, 102,  92,
        83,  94,  84, 104, 103,  98,  85,  91, 124,  90, 107, 103,  91,
       124,  87, 104, 103, 112,  98,  91, 121,  95, 100, 104, 100,  95,
       103, 109,  98,  93, 103,  95, 103,  94, 100, 101,  97,  89,  96,
       102,  98, 109, 100, 102, 117, 104, 100, 123, 108,  96, 106, 109,
        99, 111,  91, 113,  80,  98,  94,  88,  90,  96,  91, 100,  83,
       103, 112,  89,  95, 107, 110, 102, 105,  78,  93,  98, 110, 122,
        96, 104, 121, 117, 122, 117, 113,  84,  98, 108,  84,  99, 101,
        98,  99, 101, 101,  88, 109,  85,  86, 110, 119,  82,  97,  84,
       100,  89, 109, 104, 102,  98, 116,  90, 106,  93, 108,  99, 105,
       101,  88,  82,  97, 110, 123,  83,  90,  97, 104, 107, 104, 100,
       102,  78, 101, 103, 100, 101, 115, 104,  89,  96,  99, 100, 105,
        85,  91,  98,  94,  93,  96, 105, 100, 106,  91,  93, 113,  99,
       101,  87, 105,  83, 107,  89,  93,  92,  98,  99,  81, 111, 100,
        99, 114, 105,  78, 102,  95,  88,  85,  96,  86,  94, 116,  98,
       108,  87,  90,  94,  92, 104,  90, 105,  96, 107,  97, 118,  95,
       114,  99, 115, 108, 103,  97,  96, 118,  95, 113, 108,  97, 102,
       105,  97, 107, 113,  96, 100, 107,  76, 108,  98, 117,  94, 106,
        93, 102, 103, 111, 101, 115, 107,  91, 104,  98,  98, 114,  98,
        93, 104, 104, 100,  94, 105,  99, 103,  91, 100, 119, 106,  92,
       102,  88, 121,  98, 100,  92, 110, 101,  93,  95, 102,  97, 114,
        99, 103, 102, 106, 105,  89,  92, 105,  98, 117,  89, 106,  96,
       118, 102,  87, 104,  99, 104, 101,  90,  92, 116,  93,  92, 113,
        92,  98, 105,  94,  99, 104,  99, 101, 102, 101, 110, 120,  97,
        86, 101, 101,  91, 113,  93,  91,  84,  89, 100,  80,  88, 112,
       108, 110,  99,  90,  90, 105,  95, 111, 105,  89,  97,  88,  80,
        91,  95,  87,  84, 105,  87, 108,  83,  97,  95,  89, 104, 113,
       116,  94, 126,  93, 109,  94,  85, 103, 100, 107, 115,  95,  94,
       108, 101, 117,  96,  91,  98, 113, 127,  90, 100, 105, 116,  93,
       100,  77,  96,  83,  99,  99,  95,  81, 100, 101,  82,  85, 101,
        90,  86,  97, 102, 107,  99,  88, 102, 110,  92,  85,  97,  97,
       100, 102,  89,  98, 100, 107, 102,  92,  99,  91,  98, 107,  95,
       103, 110, 105, 100, 107,  82, 103,  96, 107, 105, 103, 106,  96,
       105, 118, 103,  89,  94,  91,  91,  97, 101, 119,  96,  89,  87,
       100,  89, 100,  97,  99, 104,  94,  95, 100,  86,  84,  93,  92,
        98,  96,  98,  78,  83,  94,  91,  95,  82,  85,  93, 101, 102,
       104,  96,  94,  88,  94,  85, 106, 104, 100, 107, 110,  89,  85,
        92,  97,  97, 111, 108, 103,  90, 104,  90, 101, 100, 102,  85,
       105,  94, 111, 106,  99,  94,  97,  89, 103,  98,  96,  97])
       
       



##Test erreurs systématiques
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

f = 1.0
sigma = 0.05
mt=100
nb=1000
Npoints=101

fig = plt.figure()
ax = fig.gca(projection='3d')

#liste = np.random.poisson(mt, nb)
liste = l 

diff_mu = np.linspace(-0.02*mt,0.02*mt,Npoints)
diff_f = np.linspace(-0.01*f,0.01*f,Npoints)

liste_mu=np.zeros(Npoints)
liste_f=np.zeros(Npoints)

moy = np.sum(liste) /nb 
print (moy)

for i in range (Npoints):
    
    liste_mu[i] = moy + diff_mu[i]
    liste_f[i] = f + diff_f[i]

liste_mu2, liste_f2 = np.meshgrid(liste_mu, liste_f)

def sommelog(mu,f):
    tot=0
    for j in range (nb):
        tot += -f*mu - ((f-1)**2)/(2*sigma**2) + liste[j]*np.log(f*mu) - np.log(fact(liste[j]))
    return (tot) 
#graphe en 3D
surface = -2 * sommelog(liste_mu2,liste_f2)
surf = ax.plot_surface(liste_mu2,liste_f2,surface-np.min(surface), cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_xlim3d(98,102.5)
ax.set_ylim3d(0.99,1.01)
ax.set_zlim3d(0,120)
ax.xaxis.set_ticks([98,99,100,101,102])
ax.yaxis.set_ticks([0.99,1.00,1.01])

for tickLabel in plt.gca().xaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().zaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
cbar =fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.ax.tick_params(labelsize=14) 
plt.show()
## calcul liste valeurs minimales pour chaque mu (long)
#print(moy)
plt.figure() 
val_mini = np.zeros(Npoints)
for n in range(Npoints):
    mutemp = liste_mu[n]
    temp = np.zeros(Npoints)
    for k in range(Npoints):
        temp[k] = sommelog(mutemp,liste_f[k]) 
    val_mini[n] = np.max(temp)
   

## plot des courbes avec et sans erreurs systematiques
liste_f1=[-2*sommelog(liste_mu[i],1) for i in range(len(liste_mu))]

plt.plot(liste_mu, -2*val_mini+2*val_mini[50],'g-',label='Avec ES')
plt.plot(liste_mu,liste_f1+2*val_mini[50],'b-',label='Sans ES')
plt.plot(moy,0,'ro')
plt.legend(prop={'size':14})
axes = plt.gca()
axes.xaxis.set_ticks(np.linspace(95,105,21))
for tickLabel in plt.gca().xaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)
plt.xlim(99,101)
plt.ylim(-1,4)    
plt.show()