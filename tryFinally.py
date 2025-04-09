try:
    file = open("sample.txt", "r")
    data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Operation completed.")
