try:
    file=open("data.txt")
except FileNotFoundError:
    print("file doesn't exists")
finally:
    print("finished")