# # new_list = [1, 2, 5, 10, 12, 13, 16, 20]
# def both_list():
#     i=0
#     a=[]
#     while i<len(list1):
#         j=0
#         while j<len(list2):
#             if list1[i]==list2[j]:
#                 if list2[i] not in a: 
#                     a.append(list1[i])
#             j=j+1
#         i=i+1
#     print(a)
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# both_list()
def empty():
    i=0
    empty=[]
    while i<len(list1):
        if list1[i]  not in empty:
            empty.append(list1[i])
        i=i+1
    print(empty)
list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
empty()