from time import sleep
from base.selenium_driver import SeleniumDriver


class BetagyInfinity(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver_=driver

    # Locators
    #_search_box = '//*[@id="tsf"]//input[contains(@title, "Search")]'
    _search_box1 = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
    _white_side = '//*[@id="searchform"]/div/div'
    _google_search = '//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]'
    _betagy_website = '//a[@href="https://www.betagy.com/"]'



    def inputSearch(self, name):
        self.sendKeys(name, self._search_box1, locatorType='xpath')
        sleep(1)

    def clickSearchButton(self):
        self.clickElement(self._google_search, locatorType='xpath')

    def performSearch(self, name):
        self.inputSearch(name)
        self.screenShot(resultMessage="ScreenShot before the Search")
        self.clickSearchButton()
        sleep(1)

    def verifyGooglePage(self):
        result=self.isElementPresent(self._search_box1, locatorType='xpath')
        return result

    def verifyBetagyWebPage(self):
        result=self.isElementPresent(self._betagy_website, locatorType='xpath')
        return result


