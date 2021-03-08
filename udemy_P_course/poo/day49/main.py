from connection import Connection
import time
from notification import Notification

INITIAL_PRICE = 24000
chrome_driver_path = "C:/Users/megaw/Desktop/Dev/chromedriver_win32/chromedriver.exe"
URL = "https://www.jumia.sn/"

connection = Connection(chrome_driver_path)

connection.open_browser(URL)
time.sleep(2)
connection.close_popup('//*[@id="jm"]/div[3]/section/button')

time.sleep(3)
connection.search_item("TWS Écouteurs Bluetooth pro5", '//*[@id="fi-q"]')

time.sleep(5)
connection.click_item('//*[@id="jm"]/main/div[2]/div[3]/section/div/article[1]/a')

time.sleep(5)
price = connection.get_item_price('//*[@id="jm"]/main/div[2]/section/div/div[2]/div[2]/div[3]/span').replace(" ", "").replace("FCFA", "")

price = int(price)

if price <= (INITIAL_PRICE - (0.1 * INITIAL_PRICE)):
    notification = Notification()
    print("Email Envoyé")
else:
    print("Pas de Promo")


