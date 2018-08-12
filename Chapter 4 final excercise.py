#Final excercises of chapter 4
#Define list

spam = ['apples','bananas','tofu','cats', 22, 25]
newlist = []

def listseperator(list):
    length = len(list)
    max = len(list) - 1
    if length > 0:
        for i in range(len(list)):
            if i == max:
                newlist.append('and ' + str(list[i]))
            else:
                newlist.append(str(list[i]) + ', ')

listseperator(spam)
str1 = ''.join(newlist)
print(str1)