from datetime import datetime, date


date_time_str = '18/09/2019'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')



print(date_time_obj)