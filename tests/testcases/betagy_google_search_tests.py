from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.scenario01 import BetagyInfinity
import unittest
import pytest
from utilities.teststatus import TestStatus

class loginTests(unittest.TestCase):
    @pytest.mark.run(order=1)
    def test_searchBetagy(self):
        baseurl = "https://www.google.com/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        #driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        tstatus = TestStatus(driver)
        btg =BetagyInfinity(driver)

        first= btg.verifyGooglePage()
        tstatus.mark(first, "Google page has been successfully loaded")

        second=btg.performSearch("Betagy")
        sleep(1)

        third=btg.verifyBetagyWebPage()
        tstatus.markFinal("test_searchBetagy", third, "Official Betagy site is listed on a result page")

        driver.quit()
