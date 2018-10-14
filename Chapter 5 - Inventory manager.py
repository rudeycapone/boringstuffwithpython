# inventory.py
def displayInventory(inventory):
    #Displays inventory - standard code from the book
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    #Create two lists, one as an editable list and the other one as a list that will be merged
    #later on. Dict1 is the list where items will be added to if they do not exist
    counter = 0
    dict0 = inventory
    dict1 = {}
    for key, value in inventory.items():
        for item in addedItems:
            if item == key:
                value += 1
                dict0[item] = value

    for item in addedItems:
        if item not in inventory:
            #If the last item iterated over is not equal to the current item, set counter to 0
            if lastItem != item:
                counter = 0
            #Add 1 to the counter, beceause always 1 item needs to be added
            counter += 1
            dict1.update({str(item): counter})
        lastItem = item

    #Merge the two dictionaries together
    dict0.update(dict1)
    return(dict0)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby', 'ruby', 'ruby', 'gold coin', 'armor', 'armor', 'gnome hat', 'dragon armor', 'dragon armor']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)

