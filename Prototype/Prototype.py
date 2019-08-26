#!/usr/bin/env python
# coding: utf-8

# ### Prototype - Especificar tipos de objetos a serem criados usando uma instância protótipo e criar novos objetos pela cópia desse protótipo
# 
# ### Mais Informações
# - https://www.geeksforgeeks.org/prototype-design-pattern/

# In[1]:


import abc


# In[2]:


class Car(metaclass=abc.ABCMeta):
    model = None
    value = None
    
    def __init__(self, model='Prototype', value='None'):
        self.model = model
        self.value = value
        
    @abc.abstractmethod
    def clone(self, model, value):
        pass


# In[3]:


class Sandero(Car):
    def clone(self, model, value):
        return Sandero(model, value)
    
    def __repr__(self):
        return 'Sandero {} - R$ {} - Memory Address: {}'.format(self.model, self.value, hex(id(self)))


# In[4]:


class Logan(Car):
    def clone(self, model, value):
        return Logan(model, value)
    
    def __repr__(self):
        return 'Logan {} - R$ {} - Memory Address: {}'.format(self.model, self.value, hex(id(self)))


# In[5]:


print('Prototypes:')

sanderoPrototype = Sandero()
loganPrototype = Logan()

print(sanderoPrototype)
print(loganPrototype)


# In[6]:


print('Sandero Instances:')

sanderoLife    = sanderoPrototype.clone('Life   ', 46990)
sanderoZen     = sanderoPrototype.clone('Zen    ', 49990)
sanderoIntense = sanderoPrototype.clone('Intense', 65490)


print(sanderoLife)
print(sanderoZen)
print(sanderoIntense)


# In[7]:


print('Logan Instances:')

loganLife    = loganPrototype.clone('Life   ', 50490)
loganZen     = loganPrototype.clone('Zen    ', 53490)
loganIntense = loganPrototype.clone('Intense', 68990)

print(loganLife)
print(loganZen)
print(loganIntense)

