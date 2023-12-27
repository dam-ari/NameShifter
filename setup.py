from setuptools import setup, find_packages

setup(
    name='PyNameShifter',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ns=pyname_shifter.main:main'
        ]
    },
    description='A simple tool for renaming files and folders.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BarBur 🦢',
    author_email='',
    url='https://github.com/dam-ari/PyNameShifter',
    install_requires=[
        # List your project dependencies here
        # 'dependency==version',
    ],
)
