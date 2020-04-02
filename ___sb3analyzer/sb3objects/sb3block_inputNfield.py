primitiveType = {
    # 0 : References to Objects etc
    1 : "",
    2 : "",
    3 : "",
    4 : "Number",
    5 : "PositiveNumber",
    6 : "PositiveInteger",
    7 : "Integer",
    8 : "Angle",
    9 : "Color",
    10 : "String",
    11 : "Broadcast",
    12 : "Variable",
    13 : "List",
}

def decodeInput(inputArr):

    isString =  isinstance(inputArr, str)

    if isString:
        # Type 0, Value | 0 might represent reference Costumes etc
        return [0, inputArr]
    else:
        if inputArr[0] >= 11:
            # Type, Value
            return [inputArr[0], inputArr[2]]
        else:
            # Type, Value
            return [inputArr[0], inputArr[1]]

def decodeField(fieldArr):
    # NameId, Reference
    return [fieldArr[0], fieldArr[1]]