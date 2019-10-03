#!/usr/bin/env python
# coding: utf-8

# ### Decorator - Agregar responsabilidades adicionais a um objeto dinamicamente. Os decoradores fornecem uma alternativa flexível à subclasse para ampliar a funcionalidade.
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/decorator
# - https://brizeno.wordpress.com/2011/08/31/decorator/

# In[1]:


import abc


# In[2]:


# Cocktail Component
class Cocktail(metaclass=abc.ABCMeta):        
    @abc.abstractmethod
    def operation(self):
        pass


# In[3]:


# Cocktail Decorator
class CocktailDecorator(Cocktail, metaclass=abc.ABCMeta):
    def __init__(self, cocktail):
        self._cocktail = cocktail
        
    @abc.abstractmethod
    def operation(self):
        pass


# In[4]:


# Some Cocktails
class Rum(Cocktail):
    def operation(self):
        print('Rum ', end='')
        
class Tequila(Cocktail):
    def operation(self):
        print('Tequila ', end='')
        
class Vodka(Cocktail):
    def operation(self):
        print('Vodka ', end='')


# In[5]:


# Some Additionals (Decorators)
class Lemon(CocktailDecorator):
    def operation(self):
        self._cocktail.operation()
        print('+ Lemon ', end='')
        
class Soda(CocktailDecorator):
    def operation(self):
        self._cocktail.operation()
        print('+ Soda ', end='')
        
class Salt(CocktailDecorator):
    def operation(self):
        self._cocktail.operation()
        print('+ Salt ', end='')
        
class Juice(CocktailDecorator):
    def operation(self):
        self._cocktail.operation()
        print('+ Juice ', end='')

class Ice(CocktailDecorator):
    def operation(self):
        self._cocktail.operation()
        print('+ Ice ', end='')


# In[6]:


cocktail1 = Rum()
cocktail1 = Lemon(cocktail1)
cocktail1 = Ice(cocktail1)

print('Cocktail 1: ', end='')
cocktail1.operation()


# In[7]:


cocktail2 = Tequila()
cocktail2 = Salt(cocktail2)
cocktail2 = Juice(cocktail2)

print('Cocktail 2: ', end='')
cocktail2.operation()


# In[8]:


cocktail3 = Vodka()
cocktail3 = Soda(cocktail3)
cocktail3 = Ice(cocktail3)

print('Cocktail 3: ', end='')
cocktail3.operation()

