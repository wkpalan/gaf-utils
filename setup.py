import setuptools
from packagename.version import Version


setuptools.setup(name='gaf-utils',
                 version=Version('0.1.0').number,
                 description='Utilities to read and manipulate gaf files',
                 long_description=open('README.md').read().strip(),
                 author='Kokulapalan Wimalanathan',
                 author_email='kokulapalan@gmail.com',
                 url='https://github.com/wkpalan/gaf-utils',
                 py_modules=['gaf'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='gaf gene ontology annotation',
                 classifiers=['Packages', 'gaf'])
