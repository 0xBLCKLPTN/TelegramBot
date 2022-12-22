import undetected_chromedriver.v2 as uc
from time import sleep
from selenium.webdriver.common.by import By
import json
import random


class Application:
    def __init__(self):
        options = uc.ChromeOptions()
        options.headless=True
        options.add_argument('--headless')
        self.driver = uc.Chrome(executable_path="./usr/local/bin/chromedriver", options=options)
        self.EnterToSite()
        
    def EnterToSite(self):
        self.driver.get("https://seller.ozon.ru/app/registration/signin")
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div[2]/button[1]/div").click()
        sleep(2)

    def SignIn(self, phone: str):
        try:
            try:                                                                     
                self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/section/div/div/div/div/div[3]/div/div[1]/label/div/div/input").send_keys(phone)
            except:
                self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/section/div/div/div/div/div[4]/label/div/div/input")
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/section/div/div/div/div/div[4]/button/span").click()
            sleep(2)
        except:
            self.SignIn(phone)

    
    def what_the_type(self, code):
        try:
            elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/section/div/div/div/div/div[3]/label/div/div/input")
        except:
            elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/section/div/div/div/div/div[4]/label/div/div/input")

        elem.send_keys(code)
        sleep(3)
        return self.GetCookies()


    def GetCookies(self):
        cookies = self.driver.get_cookies()
        self.driver.quit()
        json_object = json.dumps(cookies, indent=4)
        fn = "".join(str(random.randint(1,10) for i in range(12)))
        with open(f"data_storage/global_cookies/temp_{fn}.json", "w") as outfile:
            outfile.write(json_object)
        return "data_storage/global_cookies/temp_" + fn + ".json"
        
        
