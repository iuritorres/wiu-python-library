from setuptools import setup

with open('README.md', 'r') as file:
    readme = file.read()

setup(
    name='wiu',
    version='0.0.8',
    license='MIT License',
    author='Iuri Torres & João Witor',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='iuri.t1000@gmail.com',
    keywords='wiu',
    description=u'A library made to practice and improve programming and english skills during our university.',
    packages=['wiu'],
    # install_requires=[''],
)