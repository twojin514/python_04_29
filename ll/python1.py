# 1. import
# 2. pip
# 3. a = 6, b = 10
# 4. 


# 5.

# for i in range(5):
#     print("*****")

# 5. 

from audioop import add
import random

animals = ["cat","dog","lion"]
def print_animals():
    while True: 
        ans = input("입력하시오: ")
        if(ans == "print"): 
            print(random.choice(animals))
            break
        else: 
            print("print를 입력해주세요")

# print_animals()

# 6.

def add_animals():
    x=input()
    if(x=="add"):
        y=input("동물을 입력하세요")
        animals.append(y)
    else:
        print("add를 입력하세요")

    for i in animals:
        print(i, end=" ")

# add_animals()

# 7.
user_info={}
user_info["name"]="HanJiHun"
user_info["role"]="lionking"

# 8.

def menu_select(*menu_names):
    for i in menu_names:
        print(i, end=" ")
    print("주문 완료 되었습니다.")


def menu_price(**menu_price):
    for k,v in menu_price.items():
        print(k, "는 ", v, "원입니다.")


menu_select('아메리카노', '자몽허니블랙티')
menu_price(아메리카노='4000', 자몽허니블랙티='5000')




