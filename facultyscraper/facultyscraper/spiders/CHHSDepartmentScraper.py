import scrapy
from rake_nltk import Rake
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

# Create rake_nltk object.
rake_nltk_var = Rake(
    min_length=1,
    max_length=3,
    include_repeated_phrases=False,
    language="english"
)

class PHSScraper(scrapy.Spider):
    # Name of spider
    name = 'PHHSSpider'

    # Start URL of department faculty page.
    start_urls = ['https://publichealth.charlotte.edu/directory/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.followLink) 
    
    # Follow the secondary link on the page. This takes you to the faculty page that is on the department page. 
    def followLink(self, response):
        temp1 = response.css('div.field.field-name-field-directory-biography')
        temp2 = temp1.css('div.field-items')
        temp3 = temp2.css('div.field-item.even')
        finalLink = temp3.css('a::attr(href)')
        yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'Public Health Sciences',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class APHCSScraper(scrapy.Spider):
    # Name of spider
    name = 'APHCSSpider'

    # Start URL of department faculty page.
    start_urls = ['https://aphcs.charlotte.edu/directory']


    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-field-directory-biography') #field-type-text-width-summary field-label-hidden ???

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.css(
            'div.field-item').get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'Department of Applied Physiology, Health, and Clinical Sciences',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class SSWScraper(scrapy.Spider):
    # Name of spider
    name = 'SSWSpider'

    # Start URL of department faculty page.
    start_urls = ['https://socialwork.charlotte.edu/about-us/faculty-and-staff-directory']


    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-field-directory-biography')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.css(
            'div.field-item').get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'School of Social Work',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class NursingScraper(scrapy.Spider):
    # Name of spider
    name = 'NursingSpider'

    # Start URL of department faculty page.
    start_urls = ['https://nursing.charlotte.edu/about-us/faculty-and-staff']


    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-field-directory-biography')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.css(
            'div.field-item').get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'School of Nursing',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

# Adjust crawler settings for the department.
process = CrawlerProcess(settings={
    "FEEDS": {
        "College of Health and Human Services.csv": {"format": "csv"},

    },
})

# Call scrapers and run
process.crawl(PHSScraper)
process.crawl(APHCSScraper)
process.crawl(SSWScraper)
process.crawl(NursingScraper)
process.start()