class ModelParam():
    def __init__(self):
        self.__id = None
        self.__unique_id = None
        self.__navisworks = None
        self.__level = None
        self.__section = None
        self.__category = None
        self.__type = None
        self.__name = None
        self.__length = None
        self.__square = None
        self.__volume = None
        self.__offset = None
        self.__offset_up = None
        self.__width = None
        self.__height = None

    def getId(self):
        return self.__id

    def setId(self, value):
        if value != '':
            self.__id = int(value)
        else:
            raise Exception("Id cannot be empty")

    def getUniqueId(self):
        return self.__unique_id

    def setUniqueId(self, value):
        if value != '':
            self.__unique_id = str(value)
        else:
            raise Exception("UniqueId cannot be empty")

    def getNavisworks(self):
        return self.__navisworks

    def setNavisworks(self, value):
        if value != '':
            self.__navisworks = str(value)

    def getLevel(self):
        return self.__level

    def setLevel(self, value):
        if value != '':
            self.__level = str(value)

    def getSection(self):
        return self.__section

    def setSection(self, value):
        if value != '':
             self.__section = int(value)

    def getCategory(self):
        return self.__category

    def setCategory(self, value):
        if value != '':
            self.__category = str(value)

    def getType(self):
        return self.__type

    def setType(self, value):
        if value != '':
            self.__type = str(value)

    def getName(self):
        return self.__name

    def setName(self, value):
        if value != '':
            self.__name = str(value)

    def getWidth(self):
        return self.__width

    def setWidth(self, value):
        if value != '':
            self.__width = round(float(value),2)

    def getLength(self):
        return self.__length

    def setLength(self, value):
        if value != '':
            self.__length = str(value)

    def getHeight(self):
        return self.__height

    def setHeight(self, value):
        if value != '':
            self.__height = round(float(value),2)

    def getSquare(self):
        return self.__square

    def setSquare(self, value):
        if value != '':
            self.__square = str(value)

    def getVolume(self):
        return self.__volume

    def setVolume(self, value):
        if value != '':
            self.__volume = str(value)

    def getOffset(self):
        return self.__offset

    def setOffset(self, value):
        if value != '':
            self.__offset = round(float(value),2)

    def getOffsetUp(self):
        return self.__offset_up

    def setOffsetUp(self, value):
        if value != '':
            self.__offset_up = round(float(value), 2)

    def toDict(self):
        return dict({
            "id": self.__id,
            "unique_id": self.__unique_id,
            "navisworks": self.__navisworks,
            "level": self.__level,
            "section": self.__section,
            "category": self.__category,
            "type": self.__type,
            "name": self.__name,
            "length": self.__length,
            "square": self.__square,
            "volume": self.__volume,
            "offset": self.__offset,
            "offset_up": self.__offset_up,
            "width": self.__width,
            "height":self.__height
        })

    def toList(self):
        return [
            self.__id,
            self.__unique_id,
            self.__navisworks,
            self.__level,
            self.__section,
            self.__category,
            self.__type,
            self.__name,
            self.__length,
            self.__square,
            self.__volume,
            self.__offset,
            self.__offset_up,
            self.__width,
            self.__height
        ]
