from setuptools import setup, find_packages
import sys, os

setup(name='gym-seasun',
    version='0.0.1',
    description='Gym Env for Seasun Games',
    url='https://github.com/ksieee/gym_seasun',
    author='Shane Li',
    author_email='ksieee@gmail.com',
    license='Apache V2 License',
    packages=[package for package in find_packages() if package.startswith('gym_')],
    package_data={ 'gym_envs_seasun': ['lua/*.lua', 'roms/*.nes' ] },
    zip_safe=False,
    install_requires=[ 'gym>=0.8.0' ],
)