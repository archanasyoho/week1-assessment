#!/usr/bin/env python
# coding: utf-8

# ## Employee Data Analysis

# ### Analysis 1: 
# Finance has the highest average salary among the four departments.

# ![bar_chart.png](attachment:bar_chart.png)

# ### Analysis 2:
# Salaries are spread across several salary levels, with a smaller number of higher-paid employees

# ![histogram.png](attachment:histogram.png)

# ### Analysis 3:
# Employee ID does not show a meaningful relationship with salary.

# ![scatter_chart.png](attachment:scatter_chart.png)

# ### Analysis 4:
# Average salary differs by department, with Finance having the highest average.
# 

# ![line_chart.png](attachment:line_chart.png)

# In[4]:


import timeit
get_ipython().run_line_magic('timeit', '[x * 2 for x in range(1,10000)]')

