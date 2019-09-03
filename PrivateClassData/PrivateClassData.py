#!/usr/bin/env python
# coding: utf-8

# ### Private Class Data - Tem o objetivo de restringir o acesso à atributos da classe
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/private_class_data

# In[1]:


class Wallet:
    def __init__(self, id, value):
        self.id = id
        self.__value = value

    def getValue(self):
        return self.__value

    def addFunds(self,value_added):
        self.__value+=value_added


# In[2]:


my_wallet = Wallet("001", 100)

try:
    print('>> Printando atributos...')
    print(my_wallet.id)
    print(my_wallet.__valor)
except Exception as ex:
    print(ex)

print('>> Printando e modificando atributos privados...')
print(my_wallet.getValue())
my_wallet.addFunds(50)
print(my_wallet.__dict__)

