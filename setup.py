from setuptools import setup


with open('requirements.txt', 'rt') as f:
    requirements_list = [req[:-1] for req in f.readlines()]

setup(
    name='GooFee',
    version='0.2.3',
    packages=['goofee', 'goofee.core', 'goofee.action', 'goofee.events'],
    url='https://gitlab.com/jeferson.lima/GooFee',
    license='',
    author='Jeferson Lima',
    author_email='jeferson@keemail.me',
    description='A simple library to show the google calendar feed on polybar bar.',
    install_requires = requirements_list)
