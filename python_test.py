x = [100,110,120,130,140,150]
y=[n*5 for n in x]
print(y)

def divisible_by_three (n):
    n = (1,30)
    for i in n:
        if i%n==0:
            print(i)
        else:
            print(n)    

def join_list(x):
    x=[item for sublist in x for item in sublist]
    return x
    x=join_list([[1,2],[3,4],[5,6]])
    print(x)

def smallest(x):
    return min(x)
    print(smallest({3,6,8,2,4,1,5,7}))    

def divisible_by_seven ():
    n=[]
    for r in range(100,200):
        if r%7 ==0:
            n.append(r)
            return n
            k = divisible_by_seven(r)
            print(k)


def sort_list(x):
    new_set=set(x)
    return list(new_set)
    print(sort_list(x = ['a','b','a','e','d','b','c','e','f','g','h']))



        
# def greetings ():
#     students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, 
#     {"age": 22, "name": "Asha"}]
#     k = students
#     year = 2021
#     for k in students:
#         print(f"hello {name}, you were born in {year-age}")