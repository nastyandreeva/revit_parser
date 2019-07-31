from Model.ModelParam.ModelParamCollection import ModelParamCollection
from Model.ModelParam.ModelParamEntity import ModelParamEntity
from Model.ModelParam.ModelParamParser import ModelParamParser
import json


test = ModelParamParser(r'C:\Users\anastasiya.andreeva\PycharmProjects\untitled\excel')
n = test.getCollection()
#print(n.toJSON())

with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(n.toDict(), f, sort_keys=True, ensure_ascii=False, indent=4)

# test = open('C:\Users\andre\Desktop\Project\Fusion\properties.json', encoding='UTF8')
# print(test)


