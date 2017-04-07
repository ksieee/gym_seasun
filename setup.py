from setuptools import setup, find_packages
import sys, os

# Don't import gym module here, since deps may not be installed
for package in find_packages():
    if 'gym_' in package:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), package))
from package_info import USERNAME, VERSION

setup(name='gym-seasun',
    version=VERSION,
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