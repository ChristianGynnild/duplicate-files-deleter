import os

files = os.listdir()

def read_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data

files.sort(key=read_file)

duplicates = []

for i in range(len(files)-1):
    if read_file(files[i])==read_file(files[i+1]):
        duplicates.append(files[i+1])

if len(duplicates)==0:
    print(f"No duplicates found in {os.getcwd()}")
    exit(0)

print(f"{len(duplicates)} duplicates found in {os.getcwd()}:")
print("--------------")
for duplicate in duplicates:
    print(duplicate)
print("--------------")
while True:
    response = input(f"Delete the {len(duplicates)} duplicates in {os.getcwd()}? (y/n):")

    if response == "y":
        print("Deleting duplicate files")
        for duplicate in duplicates:
            print(f"Removeing {duplicate}")
            os.remove(duplicate)
        print(f"Succesfully deleted {len(duplicates)} duplicates")
        exit(0)
    elif response == "n":
        print("Operation canceled. Exiting...")
        exit()

    print("Invalid response.")
