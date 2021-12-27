import subprocess

for i in range(256):
    decoded_byte = i.to_bytes(1, "little")
    with open("flag.png", "wb") as file:
        file.write(decoded_byte)
        
    subprocess.call(["./crina"])
    with open("flag.enc", "rb") as file:
    	encoded_byte = file.read()

for i in range(256):
    decoded_byte = i.to_bytes(1, "little")
    with open("flag.png", "wb") as file:
        for i in range(6):
        	file.write(decoded_byte)
        
    subprocess.call(["./crina"])
    with open("flag.enc", "rb") as file:
    	byte = file.read()
    	print(len(byte))
    	for j in byte:
    		print(j, sep=" ", end=" ")
    	print()
    	print("***")
