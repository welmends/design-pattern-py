#!/usr/bin/env python
# coding: utf-8

# ### Bridge - Desacoplar uma abstração da sua implementação, de modo que as duas possam variar independentemente.
# 
# ### Mais informações:
# - https://sourcemaking.com/design_patterns/bridge
# - https://brizeno.wordpress.com/2011/10/13/mao-na-massa-bridge/

# In[1]:


import abc


# In[2]:


# Pane Interface
class ImplementedPane(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation_implemented(self, pane_type):
        pass


# In[3]:


# Pane Implementations (Operating Systems)
class LinuxPane(ImplementedPane):
    def operation_implemented(self, pane_type):
        print('Implementing Linux {}..'.format(pane_type))
        
class MacOSPane(ImplementedPane):
    def operation_implemented(self, pane_type):
        print('Implementing MacOs {}..'.format(pane_type))


# In[4]:


# Abstract Pane
class AbstractPane(metaclass=abc.ABCMeta):
    def __init__(self, implemented):
        self._implemented = implemented
    
    @abc.abstractmethod
    def operation(self):
        pass


# In[5]:


# Types of Pane
class BorderPane(AbstractPane):
    def operation(self):
        self._implemented.operation_implemented('BorderPane')
        
class GridPane(AbstractPane):
    def operation(self):
        self._implemented.operation_implemented('GridPane')


# In[6]:


print('>> BorderPane implemented on Linux:')
pane = BorderPane(LinuxPane())
pane.operation()
print(' ')

print('>> BorderPane implemented on MacOS:')
pane = BorderPane(MacOSPane())
pane.operation()
print(' ')

print('>> GridPane implemented on Linux:')
pane = GridPane(LinuxPane())
pane.operation()
print(' ')

print('>> GridPane implemented on MacOS:')
pane = GridPane(MacOSPane())
pane.operation()
print(' ')

