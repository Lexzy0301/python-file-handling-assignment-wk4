#filename and handle errors
try:
    file = open("twl.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
