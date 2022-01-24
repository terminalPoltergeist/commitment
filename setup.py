from setuptools import setup
setup(
    name = 'commitment',
    version = '0.0.1',
    packages = ['commitment'],
    license = 'MIT',
    url = 'https://github.com/terminalPoltergeist/commitment',
    entry_points = {
        'console_scripts': [
            'commitment = commitment.__main__:main'
        ]
    })
