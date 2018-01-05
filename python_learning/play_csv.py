def getNameList(input):
    INPUT = input
    START_INDEX = [0]
    # get index
    for i, ch in enumerate(INPUT):
        if ch.isupper() is True:
            START_INDEX.append(i)

    END_INDEX = START_INDEX[1:]
    END_INDEX.append(len(INPUT))
    WORD_LIST = []
    for i in range(len(START_INDEX)):
        WORD_LIST.append(INPUT[START_INDEX[i]:END_INDEX[i]].upper())
    return WORD_LIST

def getName(name_list):
    name = ""
    for i in range (len(name_list)):
        name += (name_list[i] + "_")
    return name

def getStatement(originalName, NAME):
    STATE = ["START", "SUCCESS", "FAILURE"]
    for i in range(len(STATE)):
        nameState = NAME + STATE[i]
        # export
        print(nameState + ",")
            

def ConvertToCaptial(input):
    NAME_LIST = getNameList(input)
    name = getName(NAME_LIST)
    getStatement(input, name)

requestNameList = ['createMyRmaCredit','updateMyRmaCredit','queryRmaCredit']

print('import {')
for i in range(len(requestNameList)):
#     print('// ' + requestNameList[i])
    ConvertToCaptial(requestNameList[i])
print("} from \'./rma/actions\'")
