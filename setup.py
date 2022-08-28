from setuptools import setup, find_packages

setup(
    name='passbird',
    version='0.0.1',
    license="MIT",
    description="Python Password Generator - Generate strong and secure passwords!",
    author="jrt345",
    url="https://github.com/jrt345/PassBird",
    packages=find_packages(),
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
            'passbird = passbird.passbird:main'
        ]
    }
)
