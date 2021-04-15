import json
from pprint import pprint

import pandas

content = pandas.read_csv('cafe-data.csv')
# data = pandas.DataFrame(content)
dicts = content.to_dict()
list = []

for item in dicts:
    list.append(dicts[item])

# print(list[0])
for item in list:
    print(item[3])

# for dict in range(len(list)):
#     for i in range(len(list[dict])):
#         print(list[dict][i])
    # for item in range(len(dict)):
    #     print(dict[item])
# for i in list:
#     for key in i:
#         print(i[key])
# for item in content:
#     for i in content[item]:
#         print(i)









# new_data_frame = pandas.DataFrame({
#     "Cafe Name": ["Boss"],
#     "Location": ["WONE"],
#     "Open": ["Test"],
#     "Close": ["24h0"],
#     "Coffee": ["Extrat"],
#     "Wifi": ["5G"],
#     "Power": ["Goku"]
# })
# # test = data.append(new_data_frame, ignore_index=True)
# test.to_csv("test.csv", mode="a", header=False)
# dict = {
#     "Cafe Name": "Boss",
#     "Location": "WONE",
#     "Open": "Test",
#     "Close": "24h0",
#     "Coffee": "Extrat",
#     "Wifi": "5G",
#     "Power": "Goku"
# }
# new_item = "\n"
# for key in dict:
#     new_item += dict[key] + ','

# print(new_item)
# t = 'Mare Street Market,https://goo.gl/maps/ALR8iBiNN6tVfuAA8,8AM,1PM,yy,bb,tt'
# with open('test.csv', "a") as file:
#     file.write(t+"\n")
