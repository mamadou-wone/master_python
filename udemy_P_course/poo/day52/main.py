from instagram import Instagram
import time

instagram_url = "https://www.instagram.com/"

instagram = Instagram(instagram_url)
time.sleep(2)

phone_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
psw_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
btn_xpath = '//*[@id="loginForm"]/div/div[3]/button/div'

instagram.connection(phone_xpath, psw_xpath, btn_xpath)

time.sleep(2)

search_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
time.sleep(2)
b_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a'
time.sleep(2)
instagram.search_user(search_xpath, b_xpath)
time.sleep(2)

suscriber_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
suscriber_btn_class = "sqdOP  L3NKy   y3zKF     "

while True:
    instagram.follow_users(suscriber_xpath)