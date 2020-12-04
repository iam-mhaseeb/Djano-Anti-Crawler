import  io
from setuptools import setup

with io.open('readme.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='django_anti_crawler',
      version='0.2',
      description='A light weight anti crawler app for Django.',
      long_description=readme,
      long_description_content_type='text/markdown',
      keywords='python, django, anti_crawler',
      url='https://github.com/iam-mhaseeb/Djano-Anti-Crawler',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['django_anti_crawler'],
      zip_safe=False,
      include_package_data=True
)
