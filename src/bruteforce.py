import time
import os

def kalku(kata,key,keynum):
    a = 0
    for i in range(len(kata)):
        a = a + int(keynum[key.index(kata[i])]) * (10**(len(kata) - 1 - i))
    return a

counter = 1
katahasil = ""
katastorage = []
hurufpertama = ""


name = str(input("Masukkan nama file: "))
cur_path = os.path.dirname(__file__)
new_path = os.path.relpath('..\\test\\' + name, cur_path)
f = open(new_path,"r")
kata = f.readline()
kata = kata.rstrip('\n')

while(kata[len(kata)-1] != "+"):
    katahasil = katahasil + kata
    katastorage.append(kata)
    hurufpertama = hurufpertama + kata[0] 
    kata = f.readline()
    kata = kata.rstrip('\n')
kata2 = kata
kata = kata[:-1]
katahasil = katahasil + kata
katastorage.append(kata)
hurufpertama = hurufpertama + kata[0] 

garis = f.readline()
garis = garis.rstrip('\n')
kata3 = f.readline()
kata3 = kata3.rstrip('\n')
f.close()

start_time = time.time()

katahasil = katahasil + kata3
hurufpertama = hurufpertama + kata3[0]

key = ['*']
for i in range(len(katahasil)):
    if(key.count(katahasil[i]) == 0):
        key.append(katahasil[i])
keynum = "1" + ("0" * (len(key) - 1))
keynum2 = keynum[1:]

angkapertama = []
for i in range(len(hurufpertama)):
    angkapertama.append(keynum[key.index(hurufpertama[i])])

total = 0
for i in range(len(katastorage)):
    total = total + kalku(katastorage[i],key,keynum)

while((keynum[0] == '1') and ((total != kalku(kata3,key,keynum)) or (len(keynum2) != len(set(keynum2))) or (angkapertama.count('0') != 0))):
    keynum = str(int(keynum) + 1)
    keynum2 = keynum[1:]
    counter = counter + 1
    
    angkapertama = []
    for i in range(len(hurufpertama)):
        angkapertama.append(keynum[key.index(hurufpertama[i])])
    
    total = 0
    for i in range(len(katastorage)):
        total = total + kalku(katastorage[i],key,keynum)

for i in range(len(katastorage) - 1):
    print(katastorage[i])
print(kata2)
print(garis)
print(kata3)        
print('\n')

if(keynum[0] == '1'):
    print('Solusi:\n')
    for i in range(len(katastorage) - 1):
        print(kalku(katastorage[i],key,keynum))
    print(str(kalku(kata,key,keynum)) + "+")
    print(garis)
    print(kalku(kata3,key,keynum))
    print('\n')
else:
    print('Tidak ada solusi yang memenuhi\n')

print('Jumlah tes yang dilakukan:',counter,'kali')
print("Waktu eksekusi: %.10f detik" % (time.time() - start_time))
