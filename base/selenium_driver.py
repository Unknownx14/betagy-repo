from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
import logging
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def screenShot(self, resultMessage):
        fileName= resultMessage + "." + str(round(time.time() *1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName= screenshotDirectory + fileName
        currentDirectory= os.path.dirname(__file__)
        destinationFile= os.path.join(currentDirectory, relativeFileName)
        destinationDirectory= os.path.join(currentDirectory, screenshotDirectory )

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver_.save_screenshot(destinationFile)   # this line saves a screenshot
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception occured")
            print_stack()


    def __init__(self, driver):
        #self.switch_to = driver1
        self.driver_=driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType== 'xpath':
            return  By.XPATH
        elif locatorType== 'name':
            return  By.NAME
        elif locatorType== 'css':
            return  By.CSS_SELECTOR
        elif locatorType== 'class':
            return  By.CLASS_NAME
        elif locatorType== 'link':
            return  By.LINK_TEXT
        else:
            self.log.info('Type ' + locatorType +' is not supported')
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType=locatorType.lower()
            byType= self.getByType(locatorType)
            element= self.driver_.find_element(byType, locator)
            self.log.info('The element has been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - The element has NOT been found with locator: ' +locator + ' and locatorType: ' + locatorType)
        return element


    def clickElement(self, locator, locatorType='id'):
        try:
            element= self.getElement(locator, locatorType)
            element.click()
            self.log.info('Clicked on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - Cannot click on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
            print_stack()

    def sendKeys(self, data,  locator, locatorType='id'):
        try:
            element= self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info('Sent data ' + data + ' on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
        except:
            self.log.info('!!!RED FLAG - Cannot send data ' + data + ' on the element with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
            print_stack()


    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info('Element is present with the locator: ' + locator+ ' and  locatorType: ' + locatorType)
                return True
            else:
                return False
        except:
            self.log.info('Element is NOT present with the locator: ' + locator+ ' and  locatorType: ' + locatorType )
            return False

