#Grab input string
data = "LUM:34.29,tF:0.01,tF_B:68.39,Pa:1829.083,Mt:0.65"


import re

def parse(data):
    i = 0
    # This allows the findall function to recognize the Mt: data.
    newString = data + ","
    dict = {'light':0.0,'temp':0.0,'temp_barom':0.0,'pressure':0.0,'humidity':0.0}
    # r refers to a raw Python string
    # \:(.*?)\, is just a complicated way of saying, "Look between each colon/comma delimiting pair!"
    strData = re.findall(r"\:(.*?)\,",newString)
    while i <= len(dict):
        if i == 0:
            dict['light'] = strData[i]
        if i == 1:
            dict['temp'] = strData[i]
        if i == 2:
            dict['temp_barom'] = strData[i]
        if i == 3:
            dict['pressure'] = strData[i]
        if i == 4:
            dict['humidity'] = strData[i]
            return dict
        i = i + 1

print(parse(data))
