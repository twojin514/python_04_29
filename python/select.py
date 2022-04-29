

# total_dictionarty = {}

# while True:
#     question = input("질문을 입력해주세요: ")
#     if question == "q":
#         break
#     else:
#         total_dictionarty[question] = "" #빈 value 값을 question이라는 key값에 할당
    
    
#     for i in total_dictionarty:
#         print(i)   # i는 key 값
#         answer = input("답변을 입력해주세요: ")
#         total_dictionarty[i] = answer  
    
#     print(total_dictionarty)


from functools import total_ordering
from traceback import print_tb


total_list=[]

while True:
    question = input("질문을 입력하시오: ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])  #질문만 출력
    answer = input("답변을 입력하시오: ")
    i["답변"] = answer  # 답변이라는 key의 value가 answer에 담김
print(total_list)
    
