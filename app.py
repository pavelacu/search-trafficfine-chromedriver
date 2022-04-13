from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import monotonic, sleep, ctime
import os


'''
    Procedure: run
        Execute a selenium instance for search a carplate in the webpage traffic fine.
    parameters:    
        url_webpage: string
            URL webpage
        type_vehicle: string (1 Character)
            Type Vehicle, this a types: Particular= P, Moto= M, Comercial= C.
        car_plate: string (3 DIGITS AND 3 LETTERS)
            the car plate to search
            Example: car_plate = '000AAA'
    
    return: not return
'''

def run(url_webpage, type_vehicle='P',  plate_car='000AAA', mode=0):
    try:
        if mode == 1:  # GUI MODE: only Local PC ***** Not Working Heroku ******
                browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        else: ## HIDE MODE
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_PATH")    
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandox")
            chrome_options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)                    

        # Get Webpage
        browser.get(url_webpage)
        # HTML Select
        browser.find_element_by_xpath("//select[@name='tplaca']/option[text()='"+type_vehicle+"']").click()
        # HTML TextBox
        inputElement = browser.find_element_by_id('nplaca')
        inputElement.send_keys(plate_car)
        # HTML Submit Button
        inputElement.submit()    
        # wait load data.
        sleep(5)
        
        # Not Remmission: High Probability
        results0 = browser.find_element_by_xpath("//div[contains(@class, 'text-center w3-panel w3-green')]")
        if results0 is not None:
            print(results0.text)
        
    # Have a Traffic Fine: Low Probability
    except NoSuchElementException:
        results1 = browser.find_element_by_id('transito')
        if results1 is not None:
            #return a data from table for line
            split_result = results1.text.split("\n")
            print("Date: ",split_result[1])
            print("Location: ",split_result[2])
            print("amount: ",split_result[3])

        else:
            print('No data')
    
    # Other Errors
    except Exception as e:
        print("Something else went wrong", e)
    finally:
        browser.quit()

if __name__ == '__main__':   
    car_plate = os.environ.get("CARPLATE_EXAMPLE")    
    type_vehicle = 'P'
    url_webpage = 'http://especiales.muniguate.com/remisiones.htm'
    run(url_webpage,type_vehicle,car_plate)