from setuptools import setup

setup(
    name='graffinity',
    version='0.1.0',
    author='Pablo Ruiz, Alejandro Alonso',
    author_email='diacritica@gmail.com, alejandroalonsofernandez@gmail.com',
    packages=['graffinity'],
    url='http://pypi.python.org/pypi/graffinity/',
    license='LICENSE',
    description='Graffinity for graphs.',
    long_description=open('README.md').read(),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        "dill == 0.2.1",
    ],
)
