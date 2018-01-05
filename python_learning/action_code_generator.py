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
        print("export const " + nameState + " = " + "\'" + nameState + "\'")
        
    state = ["Start","Success","Failure"]
    # Start
    print("export function " + originalName + state[0] + "() {")
    print("\treturn {")
    print("\t\ttype: " + NAME + STATE[0])
    print("\t}")
    print("}")
    # Success
    print("export function " + originalName + state[1] + "(data) {")
    print("\treturn {")
    print("\t\ttype: " + NAME + STATE[1] + ',')
    print("\t\tpayload: {data}")
    print("\t}")
    print("}")
    # Failure
    print("export function " + originalName + state[2] + "(error) {")
    print("\treturn {")
    print("\t\ttype: " + NAME + STATE[2] + ',')
    print("\t\tpayload: {error}")
    print("\t}")
    print("}")
    
    # functionality 
    print("export function "+ originalName +"(param) {")
    print("\t// TODO Reducer")
    print("\treturn dispatch => {")
    print("\t}")
    print("}")

def ConvertToCaptial(input):
    NAME_LIST = getNameList(input)
    name = getName(NAME_LIST)
    getStatement(input, name)

requestNameList = ['createMyRmaExchange','updateMyRmaExchange','queryRmaExchange']

for i in range(len(requestNameList)):
    print('// ' + requestNameList[i])
    ConvertToCaptial(requestNameList[i])
    print('\n')
