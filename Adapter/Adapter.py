#!/usr/bin/env python
# coding: utf-8

# ### Adapter - Converter a interface de uma classe em outra interface, esperada pelo cliente. O Adapter permite que interfaces incompatíveis trabalhem em conjunto.
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/adapter
# - https://brizeno.wordpress.com/2011/10/03/mao-na-massa-adapter/

# In[1]:


import abc


# In[2]:


# Target
class ImageTarget(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass


# In[3]:


# Adapters
class ImageOpenGLAdapter(ImageTarget):
    def __init__(self):
        self._imageAdaptee = ImageOpenGL()
        
    def request(self):
        self._imageAdaptee.specific_request()
        
class ImageSDLSurfaceAdapter(ImageTarget):
    def __init__(self):
        self._imageAdaptee = ImageSDLSurface()
        
    def request(self):
        self._imageAdaptee.specific_request()


# In[4]:


# Adaptees
class ImageOpenGL:
    def specific_request(self):
        print('OpenGL Image Requested!')
        
class ImageSDLSurface:
    def specific_request(self):
        print('SDL Surface Image Requested!')


# In[5]:


print('>> Requesting OpenGL Image..')
image = ImageOpenGLAdapter()
image.request()

print('>> Requesting SDL Surface Image..')
image = ImageSDLSurfaceAdapter()
image.request()

