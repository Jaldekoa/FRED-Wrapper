from setuptools import setup, find_packages

setup(name="FRED_Wrapper",
      version="1.0.0",
      description="A Python wrapper to easily retrieve data from the FRED website in Pandas format without using the official API.",
      long_description="FRED_Wrapper provides a way to get data from the FRED web page. Instead of using the official API, this class makes direct requests to the web page and gets the data in CSV format.",
      url="https://github.com/Jaldekoa/FRED-Wrapper",
      author="Jon Aldekoa",
      author_email="jaldekoa@gmail.com",
      license="GPL-3.0",
      packages=find_packages(include=['FRED_Wrapper', 'FRED_Wrapper.*']),
      python_requires=">=3.8",
      install_requires=["setuptools>=68.2", "pandas>=2.0.0", "requests>=2.23.0"],
      zip_safe=False)
