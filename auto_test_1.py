#Logowanie poprawne dane
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= 'C:\Test files\chromedriver.exe')
driver.get("https://profil.wp.pl/login.html?zaloguj=poczta")

assert  "Poczta - Najlepsza Poczta, największe załączniki - WP" in driver.title

time.sleep(5)

elem = driver.find_element_by_name("login_username")
elem.clear()
elem.send_keys("dawid.pytlinski.1991@wp.pl")
time.sleep(5)
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("pytla1991")
elem = driver.find_element_by_xpath ('//*[@id="btnSubmit"]') .click()

assert  "@wp (1366) Odebrane - WP Poczta" not in driver.page_source

time.sleep(5)

#elem = driver.find_element_by_id('//*[@id="Logout-Button"]').click()

#driver.close()

#Logowanie niepoprawne dane

driver.get("https://profil.wp.pl/login.html?zaloguj=poczta")
elem = driver.find_element_by_name("login_username")
elem.clear()
elem.send_keys("admin2")
time.sleep(5)
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("321")
elem = driver.find_element_by_xpath ('//*[@id="btnSubmit"]') .click()

time.sleep(5)

driver.get("https://wiadomosci.wp.pl/prognoza-pogody-cieply-poczatek-tygodnia-potem-drastyczny-spadek-temperatur-6367833756764289a")
#Logowanie niepoprawne dane






























