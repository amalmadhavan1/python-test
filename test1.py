data = [15,20,50,16,1]

def find_rem(data):
    reminders = [i%5 for i in data]
    return reminders


print(find_rem(data))


a = [26,37] / 5

b = [1,2]

c = [26,18,5]

def find_quotient(list1,list2):
    result = []
    if len(list1) != len(list2):
        return "lenght of lists is not equal "
    for i in range(len(list1)):
       res = list1[i]//list2[i]
       result.append(res)
    return result

