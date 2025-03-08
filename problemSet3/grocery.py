import sys
def main():
    grocery_items = []
    while True:
        try:
            groc = input().upper()
            grocery_items.append(groc)
            grocery_items.sort()
        except IndexError:
            pass
        except (EOFError, ValueError):
            break
    if len(grocery_items) != 0:
        unique_dict = {grocery_items[0]: 0}
        for item in grocery_items:
            duplicate = True

            for dictitem in unique_dict:
                if dictitem == item:
                    unique_dict[item] += 1
                    duplicate = False

            if duplicate:
                unique_dict[item] = 1

        for dictitem in unique_dict:
            print(f"{unique_dict[dictitem]} {dictitem}")



main()
