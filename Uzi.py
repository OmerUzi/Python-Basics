def is_polindrom(Text): #task 1
    counter=1
    for char in Text[:int(len(Text)/2)]:
        if char != Text[0-counter]:
            return False
        counter=counter+1
    return True
 

def print_num(My_List): #task 2
    counter=1
    for num in My_List:
        if num>0 and counter%2==0:
            print(num,end=" ")
        counter=counter+1


def sort(My_List):  #task3
    counter=1
    for num in My_List[1:]:
        for x in range(0,counter):
            if My_List[x]>num:
                My_List.pop(counter)
                My_List.insert(x,num)
                break
        counter=counter+1
    return(My_List)

#! /usr/bin/python3

import sys
import itertools
from hashlib import sha256
from pip._vendor.Crypto.Cipher import ARC4
from pip._vendor.colorama import *

PROOF_OF_WORK_DIFFICULTY = 25 #bit

def proof_of_work(buf,n):
    i = 0
    while True:
        for prefix in itertools.product(range(0x30,0x7E), repeat = i):
            h = sha256()
            h.update(bytes(prefix))
            h.update(buf)
            if bin(int(h.hexdigest(),16)).endswith("0"*n):
                return prefix
        i += 1

def recover_flag(solution, e_flag):
    prow = proof_of_work(solution.encode("utf8"), PROOF_OF_WORK_DIFFICULTY)
    prow = bytes(prow).decode("utf8")
    key = f"RC4KEYFILLER|{solution}|{prow}"
    key = key.encode("utf8")
    return ARC4.new(key).decrypt(e_flag)


if __name__ == "__main__":
    solution = " ".join(sys.argv[1:])
    with open("flag.txt.enc","rb") as fh:
        e_flag = fh.read()
    flag = recover_flag(solution, e_flag)
    try: 
        flag = flag.decode("utf8")
        if flag.startswith("CSA"):
            print("Congratulations!")
            print("Your flag is: ", flag)
        else:
            print("Sorry, try again")
    except:
        print("Sorry, try again")

# python3 submit.py Germain scales Franklin abacus Curie telescope Lovelace pencil Noether laptop
