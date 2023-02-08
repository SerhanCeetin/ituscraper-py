from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(name='ituscraper-py',
      version='0.1.0a1',
      description='Python library for scraping data from Istanbul Technical University websites.',
      author="SerhanCeetin",
      author_email="ceetinserhan@gmail.com",
      url="https://github.com/SerhanCeetin/ituscraper-py",
      packages=['ituscraperpy', 'ituscraperpy.sis'],
      install_requires=['requests>=2.20', 'beautifulsoup4>=4.0'],
      license="MIT",
      python_requires=">=3.8",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.10"]
      )
