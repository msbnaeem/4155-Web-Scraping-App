#import OS package
import os

#install rake_nltk onto system for keyword processor
os.system('cmd /c "pip install rake_nltk"')

#install scrapy for scrapers
os.system('cmd /c "pip install scrapy"')

#install beautifulsoup4
os.system('cmd /c "pip install beautifulsoup4"')

#install rake stopwords
os.system('cmd /c "Python -m nltk.downloader stopwords"')

#install punkt for rake
os.system('cmd /c "Python -m nltk.downloader punkt"')

os.chdir('facultyscraper/facultyscraper/spiders')

# run CCIDepartmentSpider, print to json
os.system('cmd /c "python CCIDepartmentSpider.py"')

os.system('cmd /c "python LiberalArtsDepartmentScraper.py"')


