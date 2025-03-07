def energy_formula(mass):
    ## E = mc2
    speedoflight = pow(300000000, 2)
    energy = mass * speedoflight
    return energy

def main():
    mass = int(input("Pls enter mass value in integer: "))
    energy = energy_formula(mass)
    print("Energy = ", energy)

main()
