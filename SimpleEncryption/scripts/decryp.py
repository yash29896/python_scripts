#DECRYPTOR -- DECRYPTS TARGET USING KEY
with open('key.txt',mode='r') as f:
    f.seek(0)
    key=f.read()

with open('target.txt',mode='r') as f:
    f.seek(0)
    message=f.read()

key=key.split()
message=[a for a in message]
final = [chr(int(a)+ord(b)) for a,b in zip(key,message)]
k=''
k=k.join(final)

with open('target.txt',mode='w') as f:
    f.seek(0)
    f.write(k)
    f.truncate()