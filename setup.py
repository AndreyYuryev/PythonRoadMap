from setuptools import setup
import setuptools
from os import path


def readme():
    with open(path.join(path.abspath((path.dirname(__file__))), "README.rst"), "r", encoding="utf-8") as file:
        return file.read()


setup(name='PythonRM',
      author='Andrey Yuryev',
      version='0.1',
      description='Python road map',
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      package_dir={'src': 'src'},
      # install_requires=['keyring', 'selenium', 'openpyxl'],
      include_package_data=True,
      entry_points={
          'console_scripts': ['src = src.__main__:main']
      }
      )