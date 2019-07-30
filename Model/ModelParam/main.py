from Model.ModelParam.ModelParamCollection import ModelParamCollection
from Model.ModelParam.ModelParamEntity import ModelParamEntity
from Model.ModelParam.ModelParamParser import ModelParamParser
import json


test = ModelParamParser('C:\\Users\\andre\\PycharmProjects\\revit_parser\\excel')
n = test.getCollection()
print(n.count())

# test = open('C:\Users\andre\Desktop\Project\Fusion\properties.json', encoding='UTF8')
# print(test)


with open(r'C:\Users\andre\Desktop\Project\Fusion\properties.json', encoding='utf8') as f:
    d = json.load(f)
    print(len(d['data']['collection']))
