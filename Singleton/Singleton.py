#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Singleton(object):
    _instance = None
    def __new__(self, *args, **kwargs):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self)
        return self._instance


# In[2]:


class Car(Singleton):
    def __init__(self, brand = None):
        self.brand = brand
    
    def __repr__(self):
        if self.brand is not None:
            return 'Memory Address: {} {}'.format(hex(id(self)), "Brand: " + self.brand)
        else:
            return 'Memory Address: {} {}'.format(hex(id(self)), "Brand: None")


# In[3]:


car_1 = Car('Fiat')
car_2 = Car('Toyota')

print(car_1)
print(car_2)


# In[4]:


class ConfigSysAttr(Singleton):
    def __init__(self):
        self.attr1 = 'attr1_conf'
        self.attr2 = 'attr2_conf'
        self.attr3 = 'attr3_conf'
    
    def __repr__(self):
        return 'Memory Address: {} {}'.format(hex(id(self)), 'Infos: [' + self.attr1 + ', ' + self.attr2 + ', ' + self.attr3 + ']')


# In[5]:


conf_1 = ConfigSysAttr()
conf_2 = ConfigSysAttr()

print(conf_1)
print(conf_2)


# #### Mais informações
# - https://www.opus-software.com.br/singleton-design-pattern/
# - https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
#                      
