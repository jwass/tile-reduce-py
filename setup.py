from __future__ import unicode_literals

from codecs import open as codecs_open
from setuptools import setup, find_packages


with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='tilereduce',
      version='0.0.1',
      description="Run tile-reduce map jobs in Python ",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author="Jacob Wasserman",
      author_email='jwasserman@gmail.com',
      url='https://github.com/jwass/tilereduce',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'mapbox-vector-tile>=0.1.0',
      ],
      extras_require={
          'test': ['pytest'],
      },
)
