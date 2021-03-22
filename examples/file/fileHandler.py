def reader(filepath):
    names = []
    file = open(filepath, "r")
    for row in file:
        # Luetaan tiedosto rivi riviltä
        row = row.strip()
        if row != "":
            names.append(row)
    file.close()
    return names

def writer(filepath, names):
    output = ""
    for name in names:
        output += (name + "\n")
    file = open(filepath, "w")
    file.write(output)
    file.close()

def main():
    filepath = "examples/file/names.txt"
    names = reader(filepath)
    names.append(input("Give me a name!\n"))
    writer(filepath, names)
    names = reader(filepath)
    for name in names:
        print(name)

if __name__ == "__main__":
  main()