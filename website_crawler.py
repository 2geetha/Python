# prepare for Python version 3x features and functions
from __future__ import division, print_function

import scrapy  # object-oriented framework for crawling and scraping

# function for walking and printing directory structure
def list_all(current_directory):
    for root, dirs, files in os.walk(current_directory):
        level = root.replace(current_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# examine the directory structure
current_directory = os.getcwd()
list_all(current_directory)

# list the avaliable spiders, showing names to be used for crawling
os.system('scrapy list')

# decide upon the desired format for exporting output: csv, JSON, or XML

# run the scraper exporting results as a JSON text file items.jsonlines
# this file provides text information with linefeeds to provide
# text output that is easily readable in a plain text editor
#os.system('scrapy crawl CAMPUS -o craig.csv -t csv')
os.system('scrapy crawl CAMPUS -o campus.jsonlines')
os.system('scrapy crawl LEARN -o learn.jsonlines')
os.system('scrapy crawl StANDREW -o stAndrew.jsonlines')
os.system('scrapy crawl ADAA -o adaa.jsonlines')
os.system('scrapy crawl MINDWORKS -o mindworks.jsonlines')
os.system('scrapy crawl GROWN -o grown.jsonlines')
os.system('scrapy crawl GUARDIAN -o guardian.jsonlines')
os.system('scrapy crawl UNDERSTOOD -o understood.jsonlines')

