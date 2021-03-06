#does not work

import numpy as np
import math

from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer,Dense, Activation
import tensorflow.keras as keras# as k
import tensorflow as t
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam,SGD
from tensorflow.linalg import trace





class gcomdex(Layer):#creates ordering by last param (returns indices)
  def __init__(self,gs=20,param=40,**kwargs):
    self.gs=gs
    self.param=param
    super(gcomdex,self).__init__(**kwargs)

  def build(self, input_shape):


    self.built=True


  def call(self,x):
    x=x[0]
 
    values=x[:,:,-1]#K.reshape(K.dot(x,self.metrik),(-1,self.gs))

    _,valueorder=t.math.top_k(values,k=self.gs)

    valueorder=K.cast(valueorder,"float32")

    return valueorder

    

    
  def compute_output_shape(self,input_shape):
    input_shape=input_shape[0]
    assert len(input_shape)==3
    assert input_shape[1]==self.gs
    assert input_shape[2]==self.param
    return tuple([input_shape[0],self.gs])    

  def get_config(self):
    mi={"gs":self.gs,"param":self.param}
    th=super(gcomdex,self).get_config()
    th.update(mi)
    return th
  def from_config(config):
    return gcomdex(**config)













