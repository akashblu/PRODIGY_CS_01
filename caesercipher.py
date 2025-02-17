val=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt(plaintext,key):
    c=""
    for i in plaintext:
        if i.lower() in val:
            s=val.index(i.lower())
            k=0
            k+=(s+key)%26
            c+=val[k].upper() if i.isupper() else val[k]
        else:
            c+=i
    print(c)

def decrypt(plaintext,key):
    c=""
    for i in plaintext:
        if i in val:
            s=val.index(i)
            k=0
            k+=(s-key)%26
            c+=val[k].upper() if i.isupper() else val[k]
        else:
            c += i
    print(c)  

f=True
while f:
    x=input("encrypt or decrypt:") 
    plaintext=input("enter the text:")
    key=int(input("enter the key:"))
    if x=="encrypt":
        encrypt(plaintext,key)
    if x=="decrypt":
        decrypt(plaintext,key) 
    b=input("do you want to continue yes or no:")  
    if b.lower()=="yes":
        f=True
    else:
        f=False            
              
                