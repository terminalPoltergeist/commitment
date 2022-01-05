from setuptools import setup
setup(
    name = 'commitment',
    version = '0.0.1',
    packages = ['commitment'],
    entry_points = {
        'console_scripts': [
            'commitment = commitment.__main__:main'
        ]
    })
