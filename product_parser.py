from bs4 import BeautifulSoup

from parser import Parser


class ParserProduct(Parser):
    def start(self):
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        title = self.get_title()
        price = self.get_price()
        photos = self.get_photos()
        characteristics = self.get_characteristics()
        description = self.get_description()
        link = self.url
        stars = self.get_stars()
        print(title)
        print(price)
        print(photos)
        print(characteristics)
        print(description)
        print(link)
        print(stars)

    def get_title(self):
        elements = self.soup.find_all('h1', {'data-marker': 'item-view/title-info'})
        return elements[0].text

    def get_price(self):
        elements = self.soup.find_all('span', {'data-marker': 'item-view/item-price'})
        return elements[0].text

    def get_photos(self):
        elements = self.soup.find_all('ul', {'data-marker': 'image-preview/preview-wrapper'})
        elements = elements[0].find_all('img')
        elements = [i['src'] for i in elements]
        return elements

    def get_characteristics(self):
        elements = self.soup.find_all('li', {'class': 'params-paramsList__item-_2Y2O'})
        print(elements)
        characteristics = [elements[0].text.replace("Состояние", ""),
                               elements[3].text.replace("Встроенная память: ", ""),
                               elements[5].text.replace("Состояние аккумулятора: ", "").replace('\xa0', '')]
        return characteristics

    def get_description(self):
        elements = self.soup.find_all('div', {'data-marker': 'item-view/item-description'})
        return elements[0].text

    def get_stars(self):
        elements = self.soup.find_all('span', {'class': 'style-seller-info-rating-score-C0y96'})
        return elements[0].text