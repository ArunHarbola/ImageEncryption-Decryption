import matplotlib.pyplot as plt,numpy as np,random
from numpy import zeros
i = input('Enter a jpg image. : ')
img=plt.imread(i)

rows=img.shape[0]
col=img.shape[1]

plt.title("Original Image")
plt.imshow(img)
plt.show()
key=[]
while len(key)!=256:
    j=random.randrange(0,256)
    if j not in key:
        key.append(j)
dKey = key[0]

def encrypt_image(img, key, rows, col):
    img1=np.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key[img[i][j][k]]
    return img1
e = (int)(input('Enter 0 to begin Encryption :'))
if(e==0):
    print('Encryption key for the image is : ',key)
    print("Starting Encryption")
    img1=encrypt_image(img,key,rows,col)
    plt.title("Encrypted Image")
    plt.imshow(img1)
    plt.show()
def decrypt_image(img,key, rows, col):
    img1=np.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key.index(img[i][j][k])
    return img1
o = (int)(input('Enter 1 to begin decryption : '))
if(o==1):
    d = (int)(input("Enter key to begin decryption : "))
    if(d == dKey):
        img3=decrypt_image(img1,key,rows,col)
        plt.title("Decrypted Image")
        plt.imshow(img3)
        plt.show()