from audioop import add
import random
import time

# for x in range(30):
#     print(random.choice(["된장찌개","피자","제육볶음","치킨"]))

# while True:
#     # break
#     print(random.choice(["된장찌개","피자","제육볶음","치킨"]))
#     print("is this repeat too?")
#     time.sleep(1)
#     # break



# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}

# for x,y in information.items():
#     print(x)
#     print(y)


hello = "hello lions! nice to meet you"
# print(hello[6:10])
# for i in range(5):
#     print("*****")

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


animals = ["cat","dog","lion"]

# def print_animals():



def add_animals():
    ans = input("입력하시오: ")
    if(ans == "add"):
        animal = input("추가할 동물 입력: ")
        animals.append(animal)
        for x in animals:
            print(x,end=" ")
    else:
        print("add를 입력해주세요.")

add_animals()
# for x in animals:
#     print(x,end=" ")
