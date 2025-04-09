# # Open the file in read mode
with open('example.txt', 'r') as file:
    content = file.read()

# Print the content of the file
print(content)


with open("output.txt", "w") as file: 
    file.write("Hello, Python!, this is a second test file")