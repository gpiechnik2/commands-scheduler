from setuptools import setup, find_packages


setup(
    name='commands-scheduler',
    version='1.0',
    description='A simple tool to run a given command at a specific time. Created to schedule JMeter and k6 performance test runs.',
    author='@gpiechnik2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'halo'
    ],
    entry_points={
        'console_scripts': [
            'commands-scheduler = main:schedule',
        ],
    },
)
