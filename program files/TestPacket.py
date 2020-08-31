
#we will impliment this projet with Qiskit this is only a prototype
#FOR Q_BIT
#import random 
from Packet import Packet


p1=Packet("abc",2)
print(p1)

p1.QBIT()
print(p1.Q_bit)
p1.ENCODE()
print(p1.Q_bit)
p1.DECODE()

#print(p1)

#p1.ENCODE()

#print(p1)
  
#arr=[]
#x = int(input("😀️enter N:>> "))
#x=2


#for i in range(x):
#	print(i)
#	arr.append(i)
#print("arr =",arr)
#print ("A random number from list is : ",end="")
#after mesurment we get either 0 or 1 
#y = random.choice(arr)
#print (y) 
  



""" 
import os
import hashlib 
import hmac

print(hmac.new([11001], "ABC", hashlib.sha1).hexdigest())

x="abcdef"
encoded = hashlib.sha1(x.encode()) # "abcdef" is the password
print(encoded.hexdigest())



#os.environ['PYTHONHASHSEED'] = "0"

print("=========================")
print("HASH START")
print("=========================")

a = "---"
encoded_a = hashlib.sha1(x.encode())
b = "|"
encoded_b = hashlib.sha1(x.encode())
c = "\ "
encoded_c = hashlib.sha1(x.encode())
d = "/"
encoded_d = hashlib.sha1(x.encode())
# Printing the hash values. 
# Notice Integer value doesn't change 
# You'l have answer later in article. 
#print('Hashseed is', os.environ['PYTHONHASHSEED'])
print ("The integer hash value is : " + str(encoded_a))
print ("The string hash value is : " + encoded_b.hexdigest()) 
print ("The float hash value is : " + encoded_c.hexdigest()) 
print ("The float hash value is : " + encoded_d.hexdigest())
"""


