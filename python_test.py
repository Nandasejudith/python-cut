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

# x = [[1,2],[3,4],[5,6]]

def divisible_by_seven ():
    range = (100,200)
    for r in range:
        if r%7 ==0:
            print(r)
        else:
            print(range)


        
def greetings ():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, 
    {"age": 22, "name": "Asha"}]
    k = students
    year = 2021
    for k in students:
        print(f"hello {name}, you were born in {year-age}")