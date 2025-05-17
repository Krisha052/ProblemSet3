def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = map(int, date.split("/"))
            else:
                parts = date.split(" ")
                if parts[0].isdigit():
                    continue  # first word shouldn't be a number
                month = months.index(parts[0]) + 1
                day = int(parts[1].replace(",", ""))
                year = int(parts[2])
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except (ValueError, IndexError):
            continue  # invalid input, prompt again

    print(f"{year:04}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()
