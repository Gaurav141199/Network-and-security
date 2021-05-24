import sys

filename = sys.argv[1]

f = open(filename, 'r')

input_file = f.read()

subst_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$',
              'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']
original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dic = {}

for i in range(len(subst_list)):
    dic[subst_list[i]] = original_list[i]
dic['.'] = '.'
dic[' '] = ' '
dic[','] = ','

res = ''

for e in input_file:
    res = res + dic[e]

if filename == 'cipher1.txt':
    original_list1 = ['b', 'r', 'p', 'q', 'i', 'v', 'g', 'd', 'e', 'm', 'n', 'w', 'o',
                    'j', 's', 'y', 'k', 'a', 'l', 'c', 'u', 'x', 'h', 'f', 't', 'z']
    subst_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic1 = {}

    for i in range(len(subst_list1)):
        dic1[subst_list1[i]] = original_list1[i]
    dic1['.'] = '.'
    dic1[' '] = ' '
    dic1[','] = ','

    final1 = ''

    for e in res:
        final1 = final1 + dic1[e]

    print(final1)

if filename == 'cipher2.txt':
    subst_list1 = ['a', 'g', 'c', 'n', 'w', 'q', 'x', 'z', 'v', 'p', 'f', 'd', 'u',
                    'o', 'm', 'h', 'y', 't', 'r', 'k', 'l', 'i', 'e', 's', 'b', 'j']
    original_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic1 = {}

    for i in range(len(subst_list1)):
        dic1[subst_list1[i]] = original_list1[i]
    dic1['.'] = '.'
    dic1[' '] = ' '
    dic1[','] = ','

    final1 = ''

    for e in res:
        final1 = final1 + dic1[e]

    print(final1)





