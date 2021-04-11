from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='combattbmodel',
    version='0.0.6',
    description='The COMBAT-TB model is a Chado-derived graph model',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='neo4j, genome annotation',
    url="https://github.com/COMBAT-TB/combattbmodel",
    packages=find_packages(),
    install_requires=[
        'py2neo==2021.0.1'
    ]
)
