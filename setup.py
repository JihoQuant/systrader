from setuptools import find_packages, setup

print(find_packages())

setup(
    name='systrader',
    version='1.0',
    description='System trading for Quantylab',
    author='Quantylab',
    author_email='quantylab@gmail.com',
    url='https://github.com/quantylab/systrader',
    packages=['quantylab.systrader'],
    install_requires=[
        'django', 'pywinauto'
    ]
)
