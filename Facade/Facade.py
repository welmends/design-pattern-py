#!/usr/bin/env python
# coding: utf-8

# ### Facade - Fornecer uma interface unificada para um conjunto de interfaces em um subsistema. Facade define uma interface de nível mais alto que torna o subsistema mais fácil de ser usado.
# 
# ### Mais Informações:
# - https://sourcemaking.com/design_patterns/facade
# - https://brizeno.wordpress.com/2011/11/17/mao-na-massa-facade/

# In[1]:


# Facade class
class FacadeSystem:
    def __init__(self):
        self._audiosystem = AudioSystem()
        self._videosystem = VideoSystem()

    def setup(self):
        self._audiosystem.setupChannels()
        self._audiosystem.setupFrequency()
        self._videosystem.setupColors()
        self._videosystem.setupResolution()
        print('> Sistema configurado com suscesso!', end='\n\n')
        
    def playAudio(self, audioFile):
        self._audiosystem.playAudioFile(audioFile)
        
    def renderImage(self, imageFile):
        self._videosystem.renderImageFile(imageFile)


# In[2]:


# Sub-systems (Audio and Video)
class AudioSystem:
    def setupChannels(self):
        print('> Canais Configurados!')

    def setupFrequency(self):
        print('> Frequência Configurada!')
        
    def playAudioFile(self, audioFile):
        print('Reproduzindo {}..'.format(audioFile))
        
class VideoSystem:
    def setupColors(self):
        print('> Cores Configuradas!')

    def setupResolution(self):
        print('> Resolução Configurada!')
        
    def renderImageFile(self, imageFile):
        print('Rederizando {}..'.format(imageFile))


# In[3]:


# Create a FacadeSystem Object and run its methods
system = FacadeSystem()
system.setup()
system.playAudio('music.mp3')
system.renderImage('image.png')

