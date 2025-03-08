def main():
    tank = get_fraction()

    if tank <= 1:
       print("E")
    elif tank >= 90 and tank <= 100:
       print("F")
    elif tank > 1 and tank < 90:
       print(f"{tank}%")


def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x = int(fraction[0:fraction.find("/")])
            y = int(fraction[fraction.find("/")+1: ])
            tank = check_fuel_tank(x,y)
            if tank <= 100:
                return tank

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def check_fuel_tank(x,y):
    return round((x/y) * 100)

main()
