
def main():
    groceries = []
    while True:
        try:
            item = input().strip().lower()
            groceries.append(item)
        except EOFError:
            inventory = grocery_list(groceries)
            for item in sorted(inventory):
                print(inventory[item], item.upper())
            break

def grocery_list(groceries):
    inventory = {}
    for item in groceries:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

if __name__ == "__main__":
    main()