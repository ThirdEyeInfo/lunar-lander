from setuptools import find_packages,setup

setup(
    name='lunar-lander',
    version='0.0.1',
    author='Satyaprakash Nayak',
    author_email='n.satyaprakash@yahoo.com',
    install_requires=["gymnasium","gymnasium[atari, accept-rom-license]","gymnasium[box2d]"],
    packages=find_packages()
)