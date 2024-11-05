import os

folders=input("Give the folder details with space").split()

for folder in folders:
    files=os.listdir(folder)
    print("The files in folder:", folder)
    for file in files:
        print(file)

