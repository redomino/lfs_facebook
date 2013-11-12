# python imports
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = '0.1.dev0'

setup(name='lfs_facebook',
      version=version,
      description='A tools to embed LFS on Facebook',
      long_description=README,
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: GPL License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      keywords='django e-commerce online-shop facebook',
      author="Filippo Projetto",
      author_email='fili.projetto@gmail.com',
      url='http://www.redomino.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'django_facebook'
      ],
)
