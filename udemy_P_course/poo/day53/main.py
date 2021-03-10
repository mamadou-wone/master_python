from data import Data
from form import Form
URL = "https://www.expat-dakar.com/appartements-a-louer/dakar"

data = Data(URL)
form = Form()
for item in range(len(data.get_address())):
    form.add_location(data.get_address()[item], data.get_price()[item], data.list_of_links()[item])
