# -*- coding: utf-8 -*-
import os
import xlrd
import json

from Model.ModelParam.ModelParamCollection import ModelParamCollection
from Model.ModelParam.ModelParamEntity import ModelParamEntity
from class_model import *


class ModelParamParcer():
    __modelParamCollection: ModelParamCollection

    def __init__(self, path=None):
        if path is None:
            self.path = self.__getPathFromInput()
        else:
            self.path = self.__checkDir(path)

        self.__modelParamCollection = ModelParamCollection()

    # Фун-ция преобразования пути в абсолютный и проверка на существование

    def __checkDir(self, path):
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise Exception("Заданный путь не существует")
        return path

    # Фун-ция на ввод адреса
    def __getPathFromInput(self):
        return input("Введите адрес: ")

    def run(self):
        list = self.getFilesListByPath()
        self.openFiles(list)
        return self.getCollection()

    def getCollection(self):
        return self.__modelParamCollection


    # Фун-ция поиска xls файлов и вывод их в список
    def getFilesListByPath(self):
        list = []
        for file in os.listdir(self.path):
            if file.endswith(".xls"):
                list.append(os.path.join(self.path, file))
        return list

    #path = 'C:\\Users\\anastasiya.andreeva\\PycharmProjects\\untitled\\excel'
    # path = '.\\excel'
    # path = getPathFromInput()
    #path = checkDir(path)
    #list = getFilesListByPath(path)
    #print(list[5])

    # Фун-ция создания объектов коллекции
    def openFiles(self, list):
        for file in list:
            rb = xlrd.open_workbook(file)
            sheet = rb.sheet_by_index(0)
            for i in range(sheet.nrows):
                r = sheet.row_values(i)
                obj = self.createObject(r)
                self.__modelParamCollection.append(obj)

    # Фун-ция заполнения значениями объектов коллекции
    def createObject(self, r):
        obj = ModelParamEntity()
        obj.setId(r[0])
        obj.setUniqueId(r[1])
        obj.setLevel(r[3])
        obj.setNavisworks(r[2])
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
        obj.setElevation(r[15])
        return obj


test = ModelParamParcer('C:\\Users\\anastasiya.andreeva\\PycharmProjects\\untitled\\excel')
test.run()
collection = test.getCollection()
print(collection.toJSON())

    # Фун-ция создания словаря из объектов коллекции
#    n = []

   # def createDict(self, ModelParamCollection):
   #     for i in ModelParamCollection:
   #         n.append(i.toDict())
   #     return n

    # list = openFiles(list)
    # n = createDict(ModelParamCollection)

    # with open('data.json', 'w', encoding='utf-8') as f:
    #    json.dump(n, f, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)

   # """
   # csv = []
   # for i in ModelParamCollection:
   #     csv.append(';'.join(list(map(lambda x: str(x), i.toList()))))
   # print("\n".join(csv))
   #
   # json_string = json.dumps(n, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)
   # print(json_string)
   #
   # """
