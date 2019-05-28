file_name = input("Enter a file name: ")

print("Enter lines: ")

lines = []

with open(file_name , 'w') as f:
    EOF=False

    while not EOF:
        line = input()
        line = line.strip()

        if line:
            line += "\n"
            lines.append(line)
        else:
            EOF=True

    f.writelines(lines)
