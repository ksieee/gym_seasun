from setuptools import setup, find_packages

setup(
    name='gym_seasun',
    version='0.1.0',
    description='Gym Env for Seasun Games',
    url='https://github.com/ksieee/gym_seasun',
    author='Shane Li',
    author_email='ksieee@gmail.com',
    license='Apache License Version 2.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['gym>=0.8.0'],
)
