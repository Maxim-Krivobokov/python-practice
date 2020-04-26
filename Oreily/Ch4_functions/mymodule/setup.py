from setuptools import setup

""" special file for creating package for module vsearch """

# most important are name and py_modules
setup(
    name='vsearch',
    version='1.0',
    description='Custom search tool',
    author='HF Python 2e',
    author_email='hfpy2e@gmail.com',
    url='headfirstlabs.com',
    py_modules=['vsearch'],
)
