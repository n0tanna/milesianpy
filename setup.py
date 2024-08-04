from setuptools import setup, find_packages

setup(name='milesianpy',
      version="0.0.1",
      description='A math calculation package.',
      url='https://github.com/n0tanna/milesianpy.git',
      author='Anna St Germain',
      author_email='anna.stgermain885@gmail.com',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      include_package_data=True,
      classifiers=['Programming Language :: Python :: 3'],
)
