INPUT = 'getStock'
START_INDEX = [0]

# get index
for i, ch in enumerate(INPUT):
    if ch.isupper() is True:
        START_INDEX.append(i)
        print(ch)

END_INDEX = START_INDEX[1:]
END_INDEX.append(len(INPUT))
print(START_INDEX)
print(END_INDEX)

assert len(START_INDEX) == len(END_INDEX)

# get word list
WORD_LIST = []
