# Crina Reverse Question Solution

given crina and flag.enc files, we should find out what is the flag.

Using File and Strings commands, we find out useful informations about crina file; It is an x86-64 elf shared object that dynamically linked and stripped.

First We use ltrace and strace (`strace crina`) to find out what system cals and functions called from crina. strace important lines:

```
openat(AT_FDCWD, "flag.png", O_RDONLY)  = -1 ENOENT (No such file or directory)
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
write(1, "Error! No such file or directory"..., 34Error! No such file or directory!
```

This lines show that this program tried to open `flag.png` file but this file is not included. May be the flag is somewhere in flag.png :))
So we create new file named "flag.png" and run strace again:
```
openat(AT_FDCWD, "flag.png", O_RDONLY)  = 3
read(3, "\377", 8191)                   = 1
read(3, "", 8191)                       = 0
openat(AT_FDCWD, "flag.enc", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 4
write(4, "\377\376", 2)  
```

It shows us that `flag.enc` is opened after `flag.png` and the file is written by the program. May be the `flag.enc` is the encryption of `flag.png` :))

now we use [test_encoder](./test_encoder.py) script to find how this file is encrypted:
```python
for i in range(256):
    decoded_byte = i.to_bytes(1, "little")
    with open("flag.png", "wb") as file:
        file.write(decoded_byte)
        
    subprocess.call(["./crina"])
    with open("flag.enc", "rb") as file:
    	encoded_byte = file.read()
```


First, we write every byte in `flag.png` and discover how it is encoded. every byte, mapped to unique two bytes. So length of encoded file is twice the original file. so we try to encode more complex file:
```python
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
```


Runnig this script and analyzing the result, we find that every even bytes is encoded and then reversed so we should reverse every two bytes that mapped to even bytes in original file.


Now we can write a script that maps encoded bytes and decoded bytes using a dictionary and then we read `flag.enc` file by two bytes and decode bytes using the dictionary.
```python
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
```


So you can run [crina](./crina.py) script to see how every bytes mapped. after decoding bytes, we write it to [flag1](./flag1.png) file. Then we can open the file and find the flag :)))

ASIS{Cr0n4_CR1nA_and_Th3_W0rLd!}




