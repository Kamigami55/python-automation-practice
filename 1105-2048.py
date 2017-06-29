from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

url = 'https://gabrielecirulli.github.io/2048/'

browser = webdriver.Firefox()
browser.get(url)
htmlElem = browser.find_element_by_tag_name('html')
gameCount = 1
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        if browser.find_element_by_class_name('game-over') != None:
            print('Game #%s: %s' % (str(gameCount), browser.find_element_by_class_name('score-container').text.split('\n')[0]))
            gameCount = gameCount + 1
            browser.find_element_by_class_name('retry-button').click()
    except NoSuchElementException:
        continue
