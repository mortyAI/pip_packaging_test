from setuptools import setup
import setuptools

setup(
    name='sikri_ml',
    version='0.1.2',    
    description='A example Python package',
    long_description = "this is a test for whats to come",
    url='https://github.com/mortyAI/pip_packaging_test',
    author='morten grundetjern',
    author_email = 'mortengrundetjern@sikri.no',
    license='BSD 2-clause',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    py_modules=["card_type", "score_entity", "score_request"],
    install_requires=["typing","re"],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

)