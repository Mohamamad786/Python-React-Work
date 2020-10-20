#!C:\Users\mohammad\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\n")
print("Hello Mohammad, Lets Code! <br>")

def test_book(testing):
    team = (testing + " is working <br>")
    return team

def test_code(List1):
    texting = ''
    for i in List1:
        texting += (i +" is working <br>")
    return texting

print(test_book("Faraz")) # Prints Output
List5 = ["faraz", "maxx", "sara"]
print(test_code(List5))

f = open("trial.txt", "r")
for x in f:
    print(x +" is working <br>")
f.close()

p = 0

n = 42
for i in range(n):

    if n % 3 == 0:

        q = i + 4 if n < 40 else print('none')

    else:

        q = i + 40

    p += float(q) / 1000

print(p)
