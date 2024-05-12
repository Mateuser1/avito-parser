from selenium import webdriver


class Parser:
    def __init__(self, url: str):
        self.url = url
        self.browser = self.get_browser()

    def start(self):
        ...

    def get_browser(self):
        browser = webdriver.Chrome()
        browser.get(url=self.url)
        return browser

