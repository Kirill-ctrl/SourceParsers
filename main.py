from selenium.webdriver import Firefox

from web import YandexReviews, GoogleReviews, GisReviews

ABSOLUTE_PATH_TO_GECKODRIVER = "/home/kirill/PycharmProjects/ParsersAll/ParsersSource/geckodriver/geckodriver"
COMMON_DATA = {"city": "Пермь", "organisation": "Monkey Grinder"}

if __name__ == '__main__':
    YandexReviews(driver=Firefox(executable_path=ABSOLUTE_PATH_TO_GECKODRIVER),
                  data=COMMON_DATA
                  ).find()
    GoogleReviews(driver=Firefox(executable_path=ABSOLUTE_PATH_TO_GECKODRIVER),
                  data=COMMON_DATA
                  ).find()
    GisReviews(driver=Firefox(executable_path=ABSOLUTE_PATH_TO_GECKODRIVER),
               data=COMMON_DATA
               ).find()
