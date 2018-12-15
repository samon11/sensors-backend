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
            dict['light'] = float(strData[i])
        if i == 1:
            dict['temp'] = float(strData[i])
        if i == 2:
            dict['temp_barom'] = float(strData[i])
        if i == 3:
            dict['pressure'] = float(strData[i])
        if i == 4:
            dict['humidity'] = float(strData[i])
            return dict
        i = i + 1
