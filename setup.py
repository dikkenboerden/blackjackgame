from setuptools import setup, find_packages

setup(
    name='blackjack',
    extras_require={'tests':['pytest']},
    packages=find_packages(where='src'),
    package_dir={'':'src'}
)
