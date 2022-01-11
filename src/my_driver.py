from selenium import webdriver

from src.mixins import TimeDriverMixin


class Driver(TimeDriverMixin):

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver
