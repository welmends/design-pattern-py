#!/usr/bin/env python
# coding: utf-8

# ### Composite - Compor objetos em estruturas de árvore para representar hierarquia partes-todo. Composite permite aos clientes tratarem de maneira uniforme objetos individuais e composições de objetos.
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/composite
# - https://brizeno.wordpress.com/2011/09/12/mao-na-massa-composite/

# In[1]:


import abc


# In[2]:


# Component
class File(metaclass=abc.ABCMeta):
    def __init__(self):
        self._name = 'Generic File'
        
    def __repr__(self):
        return self._name
    
    def operation(self, level=0):
        print('{}|{}'.format('  '*level, self._name))


# In[3]:


# Composite (Node)
class Folder(File):
    def __init__(self, name):
        self._name = name+'/'
        self._children = []
        
    def operation(self, level=0):
        print('{}|{}'.format('  '*level, self._name))
        for i in range(len(self._children)):
            self._children[i].operation(level+1)
            
    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)


# In[4]:


# Leaf
class FilePNG(File):
    def __init__(self, name):
        self._name = name+'.png'
        
class FileMP4(File):
    def __init__(self, name):
        self._name = name+'.mp4'
        
class FileDocx(File):
    def __init__(self, name):
        self._name = name+'.docx'


# In[5]:


# Folders
folderDocs = Folder('Documents')
folderPics = Folder('Pictures')
folderVids = Folder('Videos')
folderTrip = Folder('Trip')

# Files
docx1 = FileDocx('homework')
image1 = FilePNG('house')
image2 = FilePNG('dog')
video1 = FileMP4('MaryBirthday')
video2 = FileMP4('tripWithFriends1')
video3 = FileMP4('tripWithFriends2')

# Add files to Folder Docs
folderDocs.add(docx1)
folderDocs.add(folderPics)
folderDocs.add(folderVids)

# Add files to Folder Pics
folderPics.add(image1)
folderPics.add(image2)

# Add files to Folder Vids
folderVids.add(video1)
folderVids.add(folderTrip)

# Add files to Folder Trip
folderTrip.add(video2)
folderTrip.add(video3)

# Run operation of root node
folderDocs.operation()

