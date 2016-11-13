import setuptools

setuptools.setup(name='gaf_utils',
                 version="0.1.0",
                 description='Utilities to read and manipulate gaf files',
                 long_description=open('README.rst').read(),
                 author='Kokulapalan Wimalanathan',
                 author_email='kokulapalan@gmail.com',
                 url='https://github.com/wkpalan/gaf-utils',
                 packages=['gaf'],
                 install_requires=["pytest"],
                 license='MIT',
                 zip_safe=False,
                 keywords=['gaf','gene ontology','annotation','bioinformatics'],
                 classifiers=[
                 'Development Status :: 1 - Alpha',

                'Environment :: Console',

                'Intended Audience :: Education',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',

                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',

                 'Topic :: Scientific/Engineering :: Bio-Informatics'
                 ]
                 )
