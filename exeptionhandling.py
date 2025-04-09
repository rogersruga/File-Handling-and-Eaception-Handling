try:
    with open("examplee.txt", "r") as file:
        data = file.read()

        print(data)
        
    # To print out error message if the file is not found
except FileNotFoundError:
    print("File not found. Please check the filename.")