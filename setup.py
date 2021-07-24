from setuptools import setup, find_packages

setup(name='ncdu-s3',
      version='0.3',
      description='Generate ncdu data files for S3 buckets',
      author='Umesh',
      author_email='umesh@mit.edu',
      url='http://github.com/padiauj/ncdu-s3',
      packages=find_packages(),
      install_requires=['boto3', 'click', 'ujson'],
      entry_points={'console_scripts': ['ncdu-s3 = ncdu_s3.main:main']},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console', 'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.9',
          'Topic :: System :: Systems Administration', 'Topic :: Utilities'
      ])
