import pathlib
from setuptools import setup
#from distutils.core import setup
setup(
  name = 'pandas_ui', 
  packages = ['pandas_ui'],  
  version = '0.1',      
  license='MIT License',
  description = ' pandas_ui helps you wrangle & explore your data and create custom visualizations without digging through StackOverflow. All inside your Jupyter Notebook or JupyterLab ( alternative to Bamboolib ).',  
  author = 'Arunn Thangavel',     
  author_email = 'arunnbabainfo@gmail.com', 
  url = 'https://github.com/arunnbaba/pandas_ui',   
  download_url = 'https://github.com/arunnbaba/pandas_ui/archive/v1.0.zip',
  keywords = ['Pands_ui', 'bamboolib', 'ui for pandas'],
  include_package_data=True,
  install_requires=[            
          'future',
          'ipywidgets',
          'ipython',
          'pandas',
          'qgrid',
          'traitlets',
          'pandas-profiling',
          'bokeh',
          'plotly',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.7'   
    
  ],
)