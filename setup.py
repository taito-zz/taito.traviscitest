from setuptools import find_packages
from setuptools import setup


setup(
    name='taito.traviscitest',
    version='0.0',
    description="For testing and see how Travis CI works...",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/taito/taito.traviscitest',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['taito'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-
    """)
