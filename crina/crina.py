import subprocess


d = {}
i = 0
for i in range(256):
    decoded_byte = i.to_bytes(1, "little")
    with open("flag.png", "wb") as file:
        file.write(decoded_byte)
        
    subprocess.call(["./crina"])
    with open("flag.enc", "rb") as file:
        encoded_byte = file.read()

        d[encoded_byte] = decoded_byte
        d[bytes(reversed(encoded_byte))] = decoded_byte

print("Encoding Table: ", d)


with open("flag_clone.enc", "rb") as file:
    flag = open("./flag1.png", "wb")
    while True:
        byte = file.read(2)
        if not byte:
            break
        
        if byte in d:
            flag.write(d[byte])
 

subprocess.call(["./crina"])
