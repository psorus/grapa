import numpy as np
from numpy.random import randint as rndi
from numpy.random import random as rnd

from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer,Dense,Activation,Flatten,Dropout
import tensorflow.keras as keras# as k
import tensorflow as t
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.optimizers import Adam,SGD,RMSprop
from tensorflow.keras.utils import plot_model
import json


from createmodel import objects as o
from advload import *
from adv2load import *


for mi in ["b"]:

  model=getcomp()



  ll=model.layers


  wei=[]
  nam=[]
  met=[]

  hasjumped=False
  for l in ll:
    if hasjumped==False:
      hasjumped=True
      continue
    if l._name.find("batch_norm")>-1:
      w=l.get_weights()
      ret=[]
      for e in w:
        toa=[]
        for ee in e:
          toa.append(float(ee))
        ret.append(toa)
      print(ret)
      exit()
