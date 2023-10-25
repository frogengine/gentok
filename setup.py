from setuptools import find_packages, setup

setup(
    name='libclonevoice',
    packages=find_packages(include=['libclonevoice']),
    version='0.1.0',
    description='library clone vlice',
    author='ysn',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)