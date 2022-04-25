#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
  
  
print("User Current Version:-", sys.version)


# In[9]:


git clone https://github.com/gunthercox/ChatterBot.git


# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# In[2]:


my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])


# In[3]:


small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']


# In[4]:


list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)


# In[5]:


print(my_bot.get_response("hi"))


# In[6]:


print(my_bot.get_response("i feel awesome today"))


# In[7]:


print(my_bot.get_response("what's your name?"))


# In[8]:


print(my_bot.get_response("show me the pythagorean theorem"))


# In[9]:


print(my_bot.get_response("do you know the law of cosines?"))


# In[ ]:



