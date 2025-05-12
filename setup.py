from setuptools import setup

setup(
    name='dl',
    version='0.2-dev',
    description='A command-line downloader.',
    author='Casey Dwyer',
    author_email='caseydwyer@gmail.com',
    url='https://github.com/dwyer/dl',
    license='BSD',
    scripts=['dl'],
    install_requires=[
        'futures',
    ],
)
