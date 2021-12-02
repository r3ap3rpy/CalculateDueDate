from setuptools import setup, find_packages

setup(
    name='CalculateDueDate',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='none',
    description='The homework for the Emarsys stuff.',
    long_description=open('README.md').read(),
    install_requires=[],
    url='REPOSITORY_URL',
    author='Szabó Dániel Ernő',
    author_email='r3ap3rpy@gmail.com'
)