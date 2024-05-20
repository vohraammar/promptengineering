# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:48:39 2024

@author: Brain Hacker
"""

#%%
import google.generativeai as genai
GOOGLE_API_KEY = 'AIzaSyDaZQujJc-ejLkRD11Vvx6_Sc7FbTEwvn8'
genai.configure(api_key=GOOGLE_API_KEY)
#%%
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
#%%
model = genai.GenerativeModel('gemini-pro')
#%%
import textwrap
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
#%%
response = model.generate_content("Craft an ingenious life hack or productivity tip that ingeniously simplifies or streamlines everyday tasks. Focus on practicality, originality, and ease of implementation. Ensure the solution solves a common pain point and provides a unique perspective that enhances daily efficiency")
to_markdown(response.text)
#%%
