from setuptools import setup, find_packages
import sys, os

# Don't import gym module here, since deps may not be installed
for package in find_packages():
    if '_gym_' in package:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), package))
from package_info import USERNAME, VERSION

setup(name='{}-{}'.format(USERNAME, 'gym-sw1'),
    version=VERSION,
    description='Gym Env for SW1',
    url='https://github.com/ksieee/gym_sw1',
    author='Shane Li',
    author_email='ksieee@gmail.com',
    license='Apache V2 License',
    packages=[package for package in find_packages() if package.startswith(USERNAME)],
    package_data={ '{}_{}'.format(USERNAME, 'ksieee'): ['lua/*.lua', 'roms/*.nes' ] },
    zip_safe=False,
    install_requires=[ 'gym>=0.8.0' ],
)