import json
from typing import List, Any

from Model.ModelParam.ModelParamEntity import ModelParamEntity


class ModelParamCollection():

    __collection: List[ModelParamEntity]

    def __init__(self):
        self.__collection = []
        
    def append(self, ModelParamEntity):
        self.__collection.append(ModelParamEntity)

    def count(self):
        return len(self.__collection)

    def toList(self):
        list = []
        for obj in self.__collection:
            list.append(obj.toList())
        return list

    def toDict(self):
        list = []
        for obj in self.__collection:
            list.append(obj.toDict())
        return list

    def toJSON(self):
        list = self.toDict()
        return json.dumps(list, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)
