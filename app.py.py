#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st

st.title('Interactive Text Input Example')
st.write('enter transactions details')
v0 = st.number_input(label='v0',step=1.,format="%.2f")
v1 = st.number_input(label='v1',step=1.,format="%.2f")


# In[ ]:




