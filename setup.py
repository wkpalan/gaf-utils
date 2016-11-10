import setuptools

with open('README.rst') as f:
    long_description = f.read()


setuptools.setup(name='gaf_utils',
                 version="0.1.0",
                 description='Utilities to read and manipulate gaf files',
                 long_description=long_description,
                 author='Kokulapalan Wimalanathan',
                 author_email='kokulapalan@gmail.com',
                 url='https://github.com/wkpalan/gaf-utils',
                 packages=['gaf'],
                 install_requires=[],
                 license='MIT',
                 zip_safe=False,
                 keywords='gaf gene ontology annotation',
                 classifiers=[
                 'Development Status :: 3 - Alpha',

                 'Intended Audience :: Developers',

                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7'
                 ]
                 )
