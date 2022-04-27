# Scrapping Job Offers in Craigslist

This project scrape data about Engineering job offers in New York City from [craiglist.com](https://newyork.craigslist.org/search/egr) using Scrapy, a framework for extracting the data from websites.

The project has one spider able to scrape the textual and image data of all Engineering job offers in New York City.

The textual data is available in `jobs.csv` file. The extracted images are in `images` folder.

# How to use

You will need Python 3.x to run the scripts.
Python can be downloaded [here](https://www.python.org/downloads/).

You have to install Scrapy framework:
* In command prompt/Terminal: `pip install scrapy`
* If you are using [Anaconda Python distribution](https://anaconda.org/anaconda/python): `conda install -c conda-forge scrapy`

Once you have installed Scrapy framework, just clone/download this project, access the folder in command prompt/Terminal and run the following command:

`scrapy crawl jobs -o jobs.csv`

You can change the output format to JSON or XML by change the output file extension (ex: `jobs.json`).
