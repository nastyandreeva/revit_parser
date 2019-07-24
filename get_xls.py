# -*- coding: utf-8 -*-
import os
import xlrd
import json
lst1 = []
from class_model import *


# Фун-ция преобразования пути в абсолютный и проверка на существование

def checkDir(path):
    path = os.path.abspath(path)
    if not os.path.exists(path):
        raise Exception("Заданный путь не существует")
    return path

# Фун-ция на ввод адреса
def getPathFromInput():
    return input("Введите адрес: ")

# Фун-ция поиска xls файлов и вывод их в список
def getFilesListByPath(path):
    list = []
    for file in os.listdir(path):
        if file.endswith(".xls"):
            list.append(os.path.join(path, file))
    return list


path = 'C:\\Users\\anastasiya.andreeva\\PycharmProjects\\untitled\\excel'
#path = '.\\excel'
#path = getPathFromInput()
path = checkDir(path)
list = getFilesListByPath(path)
print(list)

n = 0

def readFiles(list):
    while n<=10:
        rb = xlrd.open_workbook(list[n])
        sheet = rb.sheet_by_index(0)
        n += 1



for i in range(sheet.nrows):
    r = sheet.row_values(i)
    obj = ModelParam()
    obj.setId(r[0])
    obj.setUniqueId(r[1])
    obj.setNavisworks(r[2])
    obj.setLevel(r[3])
    obj.setSection(r[4])
    obj.setCategory(r[5])
    obj.setType(r[6])
    obj.setName(r[7])
    obj.setLength(r[8])
    obj.setSquare(r[9])
    obj.setVolume(r[10])
    obj.setOffset(r[11])
    obj.setOffsetUp(r[12])
    obj.setWidth(r[13])
    obj.setHeight(r[14])
    ModelParamCollection.append(obj)
"""
csv = []
for i in ModelParamCollection:
    csv.append(';'.join(list(map(lambda x: str(x), i.toList()))))
print("\n".join(csv))
"""

n = []
for i in ModelParamCollection:
    n.append(i.toDict())
#print(n)

json_string = json.dumps(n, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)
print(json_string)
