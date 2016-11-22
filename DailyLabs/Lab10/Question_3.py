def main():
    total = 0
    number = 0
    
    while(number != -99):
        number = int(input("Gimme a number:"))
        total += number
    total += 99
    print(total)

if __name__ == "__main__":
    main()
