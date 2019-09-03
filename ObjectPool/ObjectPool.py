#!/usr/bin/env python
# coding: utf-8

# ### Object Pool - Tem o objetivo de reduzir o tempo e custo das instanciações, reaproveitando objetos.
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/object_pool
# - http://www.csi.uneb.br/padroes_de_projetos/object_pool.html

# In[1]:


class DB:
    def __init__(self, id=None):
        self.id = id
    
    def __repr__(self):
        return 'DB Id: {} | Memory Address: {}'.format(self.id, hex(id(self)))


# In[2]:


class DBPool:
    def __init__(self, size):
        self._dbs = [DB(_) for _ in range(size)]

    def acquire(self):
        return self._dbs.pop()

    def release(self, db):
        self._dbs.append(db)
        
    def getPoolSize(self):
        return len(self._dbs)


# In[3]:


print('>> Create Pool..')
dbpool = DBPool(10)
print('Pool size: ' + str(dbpool.getPoolSize()))

print('>> Acquire 2 dbs..')
db1 = dbpool.acquire()
db2 = dbpool.acquire()
print(db1)
print(db2)
print('Pool size: ' + str(dbpool.getPoolSize()))

print('>> Release 2 dbs..')
dbpool.release(db1)
dbpool.release(db2)
print('Pool size: ' + str(dbpool.getPoolSize()))

