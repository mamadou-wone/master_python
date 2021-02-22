from twilio.rest import Client

account = "AC2f66923cc89ca72ea11f17a038d02c85"
token = "0fdce685df4e0ce5fe7ec9f091746748"

client = Client(account, token)

from_whatshapp_number = "whatsapp:+221775596731"
to_whatsapp_number = "whatsapp:+221774724175"

client.messages.create(body="Hey Boss", from_=from_whatshapp_number, to=to_whatsapp_number)

