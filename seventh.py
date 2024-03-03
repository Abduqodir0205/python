if __name__ == "__main__":
    try:
        name = input("==>")
        yosh = int(input("==>"))
    except ValueError as error:
        print(error)
        
    print("ism -", name)
    print("yosh -", yosh)