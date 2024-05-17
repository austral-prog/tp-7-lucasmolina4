def enumerate_list(lista):
   result = []
   index = 0
   for string in lista:
        if string:
            result.append(f"{index}. {string}")
            index += 1
   return result


def enumerate_backwards(list):
    return list
