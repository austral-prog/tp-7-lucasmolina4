def index_of_by_index(color, colors, index):
    for i in range(index, len(colors)):
        if colors[i] == color:
            return i
    return -1

def index_of_empty(lista):
    color = ""
    for index, i in enumerate(lista):
        if color == lista[index]:
            return index
    return -1

def index_of(color, colors):
    for index, i in enumerate(colors):
        if color == colors[index]:
            return index
    return -1

def put(word, lista):
    for index, item in enumerate(lista):
        if item == "":
            lista[index] = word
            return index
    return -1


def remove(word, lista):
    i = 0
    for index, item in enumerate(lista):
        if item == word:
            lista[index] = ""
            i += 1
    return i



