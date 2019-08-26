#!/usr/bin/env python
# coding: utf-8

# ### Builder - Separar a construção de um objeto complexo de sua representação de modo que o mesmo processo de construção possa criar diferentes representações.
# 
# ### Mais informações:
# - https://www.geeksforgeeks.org/builder-design-pattern/
# - https://brizeno.wordpress.com/2011/09/25/mao-na-massa-builder/

# In[1]:


import abc


# In[2]:


class CarProduct(metaclass=abc.ABCMeta):
    model = None
    value = None
    manufactureYear = None
    
    def __init__(self):
        pass
    
    def __repr__(self):
        return 'CarProduct\n          Model: {}, Value: R$ {}, Year of Manufacture: {} '.format(self.model, self.value, self.manufactureYear)


# In[3]:


class CarBuilder(metaclass=abc.ABCMeta):
    carProduct = CarProduct()
    
    def __init__(self):
        pass
    
    def getProduct(self):
        return self.carProduct
    
    @abc.abstractmethod
    def buildModel(self):
        pass
    
    @abc.abstractmethod
    def buildValue(self):
        pass
    
    @abc.abstractmethod
    def buildManufactureYear(self):
        pass


# In[4]:


class RenaultBuilder(CarBuilder):
    def __init__(self):
        super()
    
    def buildModel(self):
        self.carProduct.model = "Logan Zen"
        
    def buildValue(self):
        self.carProduct.value = 53490.00
    
    def buildManufactureYear(self):
        self.carProduct.manufactureYear = 2020


# In[5]:


class FiatBuilder(CarBuilder):
    def __init__(self):
        super()
    
    def buildModel(self):
        self.carProduct.model = "Argo Drive"
        
    def buildValue(self):
        self.carProduct.value = 46990.00
    
    def buildManufactureYear(self):
        self.carProduct.manufactureYear = 2020


# In[6]:


class CarDealershipDirector():
    carBuilder = None
    
    def __init__(self, carBuilder=CarBuilder):
        self.carBuilder = carBuilder
        
    def constructCar(self):
        self.carBuilder.buildModel()
        self.carBuilder.buildValue()
        self.carBuilder.buildManufactureYear()
        
    def getCar(self):
        return self.carBuilder.getProduct()


# In[7]:


carDealership = CarDealershipDirector(RenaultBuilder())
carDealership.constructCar()
print(carDealership.getCar())

carDealership = CarDealershipDirector(FiatBuilder())
carDealership.constructCar()
print(carDealership.getCar())

