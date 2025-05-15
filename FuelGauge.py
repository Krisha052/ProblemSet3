import math

def main():
    while True:
        try:
            x, z = input("Fraction: ").split("/")
            percentage = get_percentage(x, z) 
            if percentage is not None: #evaluating to 0 will result in a False when if percentage is used
                if percentage < 1:
                    print("E")
                elif percentage > 99:
                    print("F")
                else:
                    print(f"{percentage}%")
                break
        except ValueError: #in case of invalid input, however it is not a problem with the current test cases
            continue

def get_percentage(x, z):
    try:
        x, z = int(x), int(z)
        if z == 0:
            return None
        if x > z:
            return None
        return math.floor((x / z) * 100)
    except (ValueError, ZeroDivisionError): #must always make a tuple of the exceptions, can't use or
        return None

if __name__ == "__main__":
    main()
