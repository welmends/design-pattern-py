#!/usr/bin/env python
# coding: utf-8

# In[1]:


import abc


# In[2]:


class AbstractFactory(metaclass=abc.ABCMeta):
    '''
    Declare an interface for operations that create abstract product objects.
    '''

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


# In[3]:


class ConcreteFactory1(AbstractFactory):
    '''
    Implement the operations to create concrete product objects.
    '''

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

    
class ConcreteFactory2(AbstractFactory):
    '''
    Implement the operations to create concrete product objects.
    '''

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


# In[4]:


class AbstractProductA(metaclass=abc.ABCMeta):
    '''
    Declare an interface for a type of product object.
    '''

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    '''
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface.
    '''

    def interface_a(self):
        pass


class ConcreteProductA2(AbstractProductA):
    '''
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface.
    '''

    def interface_a(self):
        pass


# In[5]:


class AbstractProductB(metaclass=abc.ABCMeta):
    '''
    Declare an interface for a type of product object.
    '''

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    '''
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface.
    '''

    def interface_b(self):
        pass


class ConcreteProductB2(AbstractProductB):
    '''
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface.
    '''

    def interface_b(self):
        pass


# In[6]:


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()


# ### Mais Informações
# - http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/pat/abstractfactory.htm
