import numpy as np
import math

from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer,Dense, Activation
import tensorflow.keras as keras# as k
import tensorflow as t
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam,SGD
from tensorflow.linalg import trace





class gremoveparam(Layer):
  def __init__(self,gs=50,inn=30,out=20,**kwargs):
    assert inn>=out
    self.gs=gs
    self.inn=inn
    self.out=out
    super(gremoveparam,self).__init__(**kwargs)


  def build(self, input_shape):

    self.built=True


  def call(self,x):
    x=x[0]
    return x[:,:self.gs,:self.out] 
 

    
  def compute_output_shape(self,input_shape):
    input_shape=input_shape[0]
    assert len(input_shape)==3
    assert input_shape[-1]==self.inn
    assert input_shape[-2]==self.gs
    return tuple([input_shape[0],self.gs,self.out])    

  def get_config(self):
    mi={"inn":self.inn,"gs":self.gs,"out":self.out}
    th=super(gremoveparam,self).get_config()
    th.update(mi)
    return th
  def from_config(config):
    return gremoveparam(**config)













