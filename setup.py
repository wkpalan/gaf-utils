import setuptools


setuptools.setup(name='gaf_utils',
                 version="0.1.0",
                 description='Utilities to read and manipulate gaf files',
                 long_description=open('README.md').read().strip(),
                 author='Kokulapalan Wimalanathan',
                 author_email='kokulapalan@gmail.com',
                 url='https://github.com/wkpalan/gaf-utils',
                 packages=['gaf'],
                 install_requires=[],
                 license='MIT',
                 zip_safe=False,
                 keywords='gaf gene ontology annotation',
                 classifiers=['Packages', 'gaf']
                 )
