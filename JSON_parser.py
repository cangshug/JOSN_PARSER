import json

f = [
        {
            "id": "0001",
            "type": "desert",
            "name": "Birthday Cake",
            "brand": "A",
            "batters":
                {
                    "batter":
                        [
                            { "id": "2001", "type": "Sugar" },
                            { "id": "2002", "type": "Cinnamon" },
                            { "id": "2003", "type": "Strawberry" },
                            { "id": "2004", "type": "Banana" }
                        ]
                },
            "topping":
                [
                    { "id": "1001", "type": "None" },
                    { "id": "1002", "type": "Glazed" },
                    { "id": "1005", "type": "Sugar" },
                    { "id": "1007", "type": "Cream" }
                ]
        },
        {
            "id": "0002",
            "type": "ice cream",
            "name": "Soda Fountain",
            "flavors":
                {
                    "flavor":
                        [
                            { "id": "3001", "type": "Regular" }
                        ]
                },
            "topping":
                [
                    { "id": "1001", "type": "None" },
                    { "id": "1003", "type": "Banana" },
                    { "id": "1004", "type": "Pecan" },
                ]
        },
        {
            "id": "0003",
            "type": "donut",
            "name": "Old Fashioned",
            "brand": "B",
            "batters":
                {
                    "batter":
                        [
                            { "id": "2000", "type": "Regular" },
                            { "id": "2002", "type": "Cinnamon" }
                        ]
                }
        }
    ]   

record_count = len(f)

def batter_types(x):
    if 'batters' in f[x]:
        for i in range(len(f[x]['batters']['batter'])):
            print(f[x]['batters']['batter'][i]['type'])
    else:
        print('')


def topping_types(x):
    if 'topping' in f[x]: 
        for i in range(len(f[x]['topping'])):
            print(f[x]['topping'][i]['type'])
    else:
        print('')

x = 0
while x < record_count:
    print(f[x]['name'].upper())
    print("Batter Types:")
    batter_types(x)
    print("Topping Types:")
    topping_types(x)
    print()
    x = x + 1


