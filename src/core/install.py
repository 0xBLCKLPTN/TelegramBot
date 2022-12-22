import undetected_chromedriver as uc
from time import sleep

driver = uc.Chrome()
driver.get('https://nowsecure.nl')
sleep(10)