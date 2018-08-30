#question 1

print("<------ solution 1 ------>")
f=open('1.txt','r')
h=f.read()
print(h)

#question 2

print("<------ solution 2 ------>")
count=0
f=open('1.txt')
j=input("enter word ")
for line in f:
       count+=line.count(j)
print(count)
f.close()

#question 3

print("<------ solution 3 ------>")
with open('1.txt' ,'r') as f:
       with open('2.txt' ,'w') as f2:
              for line in f:
                     f2.write(line)
with open('2.txt' ,'r') as f2:
       print(f2.read())

#question 4

print("<------ solution 4 ------>")
f1 = open("1.txt")

f2 = open("2.txt")

f3=open("3.text",'w')
for i,j in zip(f1,f2):
       f3.write(i+j)
f3=open("3.text",'r')
print(f3.read())


#question 5

print("<------ solution 5 ------>")
f=open('1.txt')
t=open('4.txt','w+')
h=f.readlines()
h.sort()
t.write(str(h))
t.seek(0)
o=t.read()
print(o)
