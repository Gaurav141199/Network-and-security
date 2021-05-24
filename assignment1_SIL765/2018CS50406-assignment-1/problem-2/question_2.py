import random
import hashlib 

d = int(input())

def get(val, d):
    output = ''.join(format(ord(i), 'b') for i in val) 
    return output[:d]

def compare(one, two, d):
    h1 = hashlib.sha3_256(one.encode()).hexdigest()
    h2 = hashlib.sha3_256(two.encode()).hexdigest()
    h1_6 = get(h1[:6], d)
    h2_6 = get(h2[:6], d)
    if h1_6 == h2_6:
        return True
    return False   


def hey(d):
    one = ''.join(random.choices("01", k=d))
    two = ''.join(random.choices("01", k=d))

    itr = 0
    while True:
        one = ''.join(random.choices("01", k=d))
        two = ''.join(random.choices("01", k=d))
        itr += 1
        if compare(one, two, d):
            print(one)
            print(two)
            print(itr)        
            break
        h = get(hashlib.sha3_256(one.encode()).hexdigest(), d)[:6]
        print(one)
        print(two)
        print(h)
        print(1)
        print(itr)
        return (one, two, h, 1, itr)
            
hey(d)        


