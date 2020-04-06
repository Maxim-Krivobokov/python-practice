import pprint
# display inventory for rpg game


def displayInventory(inventory):
    total_items = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' of ' + str(k))
        total_items = total_items + int(v)
    print('Total number of items: ' + str(total_items))
    print('=============================')
    return total_items


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        if item in inventory.keys():
            inventory[item] = str(int(inventory[item]) + 1)
    displayInventory(inventory)
    return inventory


dragonLoot = ['gold', 'arrows', 'sword', 'torch', 'gold', 'gold', 'diamond']

warrior_inventory = {'rope': 1, 'gold': 54, 'arrows': 10,
                     'torch': '5', 'throwing axe': 8, 'sword': 2}

sorcerer_inventory = {'rope': 1, 'gold': 85, 'arrows': 3,
                      'torch': '7', 'potion': 8, 'sword': 1, 'fireball': 10}

# print(warrior_inventory.items())
# pprint.pprint(warrior_inventory)
# print(str(displayInventory(warrior_inventory)))

print('warrior inventory:')
# displayInventory(warrior_inventory)


#print('sorcerer inventory:')
# displayInventory(sorcerer_inventory)

addToInventory(warrior_inventory, dragonLoot)

print('Sourcerer got his loot:')
addToInventory(sorcerer_inventory, dragonLoot)
