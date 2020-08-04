#ENCRYPTOR --PRODUCES EXCRYPTED TEXT AND KEY
from random import randint

with open('target.txt',mode='r') as f:
    f.seek(0)
    message=f.read()

new = [a for a in message]

strb=[ord(a) for a in new]
ci=[]
l3=[]
for x in strb:
    if (x==ord('\n')):
        temp=randint(22,117)
        ci.append(-temp)
        l3.append(x+temp)
    elif x<64:
        temp=randint(32,64)
        ci.append(-temp)
        l3.append(x+temp)
    else:
        temp=randint(1,32)
        ci.append(+temp)
        l3.append(x-temp)
l3=[chr(a) for a in l3]
enc=''
for a in l3:
    enc+=a

w=''
e=''
w=[str(a) for a in ci ]

f=[]
for var in w:
    f.append(var+' ')
m=''
m=m.join(f)


b=''
for a in enc:
    b+=a  

with open('key.txt', mode='w') as f:
    f.seek(0)
    f.write(m)
    f.truncate()
with open('target.txt', mode='w') as f:
    f.seek(0)
    f.write(b)
    f.truncate()