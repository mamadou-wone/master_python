from smtplib import SMTP
class Notification:
    def __init__(self):
        self.send_notification()


    def send_notification(self):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="megawone735@gmail.com", password="775596731")
            connection.sendmail(from_addr="megawone735@gmail.com", to_addrs="mamadouwone12345@gmail.com",
                                msg="Subject:Price Alert\n\nHello Boss😎 -10% sur les TWS Allez le commander :)"
                                )