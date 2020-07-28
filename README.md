# pandas_ui  [![Downloads](https://pepy.tech/badge/pandas-ui)](https://pepy.tech/project/pandas-ui)
pandas_ui helps you wrangle &amp; explore your data and create custom visualizations without digging through StackOverflow. All inside your Jupyter Notebook ( alternative to Bamboolib ).



This tool is inspired and created as an alternative for the bamboolib since it comes with pricing.

This tool is tested and verified with windows 10, Google chrome, Python 3.7.

please read this medium article for more details: https://medium.com/@arunnbaba/pandas-ui-87316a4e19c7?sk=250429311c0655bf43a65a1cf688b966

# Who is this tool for:
It is highly sophisticated and yet easy to use tool that can be used by both the advanced and novice users. It is designed to reduce the time fo data pre-processing for data scientists and data analysts.
It is highly recommended for the python and pandas beginners.

# Getting started.

To install: 
Run command prompt

>>pip install pandas_ui

>>jupyter nbextension enable --py qgrid --sys-prefix

>>jupyter nbextension enable --py widgetsnbextension --sys-prefix

After installing, open jupyter notebook

>>from pandas_ui import *

>> pandas_ui('csv_file_path_here')

To get the dataframe after processing:

>>get_df() # to get the dataframe

>>get_meltdf() or  get_pivotdf() # to get melt or pivot dataframes if you have created any.


# Main features and benefits of Pandas_ui

# 90% less working time
Focus on what you want to do instead of how

No more digging through StackOverflow

What would you prefer a dozen of complex python code or few mouse click?.

# Easy to use
Quick onboarding with minimal learning curve

# 100% compatible and flexible
Seamless integration into your existing working environment

Work from within Jupyter Notebook or JupyterLab

# Private, secure, local
All your data remains private and secure

Use it on your local machine without the need for cloud access

Satisfies the requirements of your IT department
