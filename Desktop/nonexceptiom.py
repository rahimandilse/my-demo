path = "nonexistent.txt"

try:
    with open(path, "r") as file:
        content = file.read()
        print("Content of", path, ":\n", content)

except FileNotFoundError:
    print(" filedoes not exist. Please check the file path.")
except IOError:
    print("An error occurred while trying to read the file ")
