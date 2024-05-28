#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install konlpy')


# In[5]:


from konlpy.tag import Komoran


# In[9]:


class Preprocess:
    def __init__(self, userdic=None):
        self.komoran = Komoran(userdic=userdic)
        
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JX',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM'
            'XSN', 'XSV', 'XSA'
        ]
    
    def pos(self, sentence):
        return self.komoran.pos(sentence)
    
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list


# In[ ]:




