import sys
from math import gcd 
from math import sqrt
import time
import matplotlib.pyplot as plt 

filename = sys.argv[1]

f = open(filename, "r")

temp = f.read() 

temp_arr = temp.split('\n')

num_list = list()
x_list = list()

c = 0

for i in range(0, len(temp_arr) - 1):
    c += 1
    if c <= 50:
        x_list.append(len(temp_arr[i]))
    num_list.append(int(temp_arr[i])) 

print(num_list)

time_list = list()


filename2 = 'plaintext.txt'

f2 = open(filename2, "r")

temp2 = f2.read()

input_message = list()

for e in temp2:
    input_message.append(ord(e))

def power(x, y, p):
    #(a*b)%m = ((a%m)*(b%m))%m
    x = x%p
    answer = 1
    while y > 0:
        if y%2 == 1:
            answer = (answer*x)%p
        x = (x*x)%p
        y = y/2
    return answer
    
def factorise(n):
    primes = list()
    if n%2 == 0:
        primes.append(2)
        primes.append(n//2)
        return primes
    for i in range(3,int(sqrt(n))+1, 2):
        if n%i == 0:
            primes.append(i)
            primes.append(n//i)
            return primes
    return primes


def process(val):
    start_time = time.time()
    primes = factorise(val)
    end_time = time.time()
    time_list.append(end_time - start_time)
    phi = (primes[0] - 1)*(primes[1] - 1)
    e = 2
    while True:
        if gcd(phi, e) == 1:
            break
        else:
            e += 1
    k = 1
    d = (1 + k*phi)//e

    arr = input_message.copy()
    for i in range(len(arr)):
        M = arr[i]
        arr[i] = power(M, e, val)

    for i in range(len(arr)):
        C = arr[i]
        arr[i] = power(C, d, val)

    out = list()

    for e in arr:
        out.append(chr(e))
    
    res = ''

    for e in out:
        res += e

    print(res)
    

count = 0
for e in num_list:
    count += 1
    print(count)
    process(e)
    if count == 50:
        break

print(x_list)
print(time_list)

plt.plot(x_list, time_list) 
plt.xlabel('Number of digits') 
plt.ylabel('Time taken to factorise') 
  
plt.title('Time vs Number of digits')   
plt.show() 