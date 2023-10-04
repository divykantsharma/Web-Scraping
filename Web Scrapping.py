#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPPING 

# ## Step 0: Import the required libraries

# In[1]:


import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"


# ## Step 1: Get the HTML

# In[2]:


r=requests.get(url)
htmlContent=r.content
# print(htmlContent)


# ## Step 2: Parse the HTML (creating soup)

# In[3]:


soup=BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)


# ## Step 3: HTML tree traversal

# In[4]:


print(type(soup))   #BeautifulSoup
print(type(title))   #Tag
print(type(title.string))   #Navigable String

# Get the title of HTML page
# title=soup.title
# print(title)
# print(type(title))
# print(title.string)


# Get all the paragraphs from the page
# paras=soup.find_all('p')
# print(paras)


# Find the first para tag and it's classes
# print(soup.find('p'))  #pehla paragraph mil jaayega 
# print(soup.find('p')['class'])    #ussi paragraph ki saari classes mil jaayegi


# Find all the elements with class'text-base'
# print(soup.find_all("p",class_="text-base"))


# Get the text from tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())   # saare page ka content


# Get all the anchor tags from the page
# anchors=soup.find_all('a')
# print(anchors)


# Get all the links on the page
# for link in anchors:
#     print(link.get('href'))

