import numpy as np
import matplotlib.pyplot as plt
from os.path import isfile

bins=100
alpha=0.5

shallsv=isfile("evalsvb.npz")
shallnoise=isfile("evalnoiseb.npz")


f=np.load("evalb.npz")
if shallsv:f2=np.load("evalsvb.npz")
if shallnoise:f3=np.load("evalnoiseb.npz")


x=f["x"]
y=f["y"]
p=f["p"]
c=f["c"]


if shallsv:
  x=np.concatenate((x,f2["x"]))
  y=np.concatenate((y,f2["y"]))
  p=np.concatenate((p,f2["p"]))
  c=np.concatenate((c,f2["c"]))


if shallnoise:
  x=np.concatenate((x,f3["x"]))
  y=np.concatenate((y,f3["y"]))
  p=np.concatenate((p,f3["p"]))
  c=np.concatenate((c,f3["c"]))



y=np.abs(y)
#print(y)

#exit()

def difference(a,b):
  #print(a.shape,b.shape,np.mean(a-b).shape)
  #exit()
  return np.sqrt(np.mean((a-b)**2))

d=np.zeros((len(y),))

ds=[]
for i in range(int(np.max(y))+1):
  ds.append([])


for i in range(len(y)):
  d[i]=difference(c[i],p[i])
  ds[int(y[i])].append(d[i])

def roc(d,ds,a,b):
  d0=ds[a]
  d1=ds[b]
  cmax=np.max(d)
  cmin=np.min(d)
  cdel=(cmax-cmin)/1000
  cs=np.arange(cmin,cmax,cdel)
  tpr,fpr,tnr,fnr=[],[],[],[]

  for c in cs:
    tp,fp,tn,fn=0,0,0,0
    for ad in d0:
      if ad>c:
        fp+=1#false positive, is zero, classified as one
      else:
        tn+=1#true negative, is zero, classified as zero
    for ad in d1:
      if ad>c:
        tp+=1#true positive, is one, classified as one
      else:
        fn+=1#false negative, is one, classified as zero
    tpr.append(tp/(tp+fn))
    fpr.append(fp/(fp+tn))
    tnr.append(tn/(tn+fp))
    fnr.append(fn/(fn+tp))
  np.savez_compressed("roc"+str(a)+"-"+str(b),c=c,tpr=tpr,fpr=fpr,tnr=tnr,fnr=fnr)
  return tpr,fpr,tnr,fnr

def int(x,y):
  x,y=(list(t) for t in zip(*sorted(zip(x,y))))
  ret=0.0
  for i in range(1,len(x)):
    ret+=((y[i]+y[i-1])*(x[i]-x[i-1]))/2
  return ret

for i in range(len(ds)):
  plt.hist(ds[i],bins=bins,alpha=alpha,label=str(i))


plt.legend()

plt.xlabel("mse")
plt.ylabel("#")

plt.savefig("imgs/grecqual.png",format="png")
plt.savefig("imgs/grecqual.pdf",format="pdf")

plt.show()

plt.close()

def fullroc(d,ds,a,b):
  tpr,fpr,tnr,fnr=roc(d,ds,a,b)
  auc=int(fpr,tpr)

  plt.title("Roc curve of "+str(a)+" and "+str(b))

  plt.plot(fpr,tpr,label="auc="+str(round(auc,4)),color="darkblue")
  plt.plot(tpr,fpr,label="auc="+str(round(1-auc,4)),color="dodgerblue")

  plt.plot(np.arange(0,1,0.01),np.arange(0,1,0.01),color="grey",alpha=0.3)



  plt.legend()
  plt.xlabel("false positive rate (is true, but classified as false)")
  plt.ylabel("true positive rate (is true, and classified as true)")

  plt.savefig("imgs/roc"+str(a)+"-"+str(b)+".png",format="png")
  plt.savefig("imgs/roc"+str(a)+"-"+str(b)+".pdf",format="pdf")
  plt.show()


for i in range(len(ds)):
  if len(ds[i])==0:continue
  for j in range(i):
    if len(ds[j])==0:continue
    fullroc(d,ds,j,i)















