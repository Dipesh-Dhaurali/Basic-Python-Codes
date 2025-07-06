# read and write the binary file at once
with open('data.bin', 'ab+')as file:
    file.write(b'\z01\z02')

    file.seek(0)
    binary=file.read()
    print(binary)


