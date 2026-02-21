   
#type conversion
#a=int("3")
#b=7.62
#print(a+b) 
#name=input("enter your name:")
#print("you entered",name)2
#number=float(input("decimal value"))
#print("your decimal value is ",number)
#name=input("enter your name:")
#age=int(input("enter yopur age:"))
#marks=float(input("enter percentage:"))

#print("welcome")
#print("name:",name)
#print("age:",age)
#print("marks:",marks)
#First=int(input("enter first number:"))
#second=int(input("enter second number:"))
#print("sum=",First+second)
#side=float(input("enter side:"))
#print("area=",side*side)
#a=int(input("enter a="))
#b=int(input("enter b="))
#print(a>=b)
#str1="roman"
#str2="dhanu"
#finalstr=str1+str2
#print(finalstr)
#str="roman reigns"
#chr=str[6]
#print(chr)
#print(str[1:3])
#str = "i love india and people"
#print(str.count("o"))
#str="I am a $$$ bilionire $$$"
#print(str.count("$")

#x=int(input("enter x:"))

#if(x%7==0):
 #   print("x is multiple of 7")

#else:
 #   print("x is not multiple of 7")  
#marks=[92.8,90.8,20.8,72.8]
#print(student)
#student[0]="arjun"
#print(marks[1:4])
#tuple=(9,7,12,2,3,45,4,3,4,6,4,)
#print(tuple.index(4))
#movies=[]
#movies1=(input("enter your fav movie 1:"))
#movies2=(input("enter your fav movie 2:"))
#movies3=(input("enter your fav movie 3:"))
#print(movies1,movies2,movies3)
#Grade=["A","C","B","A","c","D","c"]
#Grade.sort()
#print(Grade)
#Student={
 #  "subject":{
  #      "phy":88,
   #     "Math":85,
    #    "C++":98,
#Student.update({"state":"delhi"})
#print(Student)
#set1={1,2,3,4}
#set2={2,3,4,5}
#print(set1.intersection(set2))
#dict={
  #   "cat":"a small animal",
 #   "table":["a piece of furniture","list of facts & figures "]
#}
#print(dict)
#subject={
 #   "python","c++","c","java","python","c++","javascript","C","python","java"
#}
#print(len(subject))

#
#value={
 #   ("float",9.0),
  #  ("int",9
#print(value)
#n=int(input("enter the number"))

#
#num=(1,4,9,16,25,36,49,64,81,100)
#x=36
#idx=0
#for el in num:
 #  if(el == x):
  #    print("found",idx)
   #   break
   #idx+=1
#n=int(input("enter num:"))
#for i in range(1,11 ):
#    print(n*i)  

#
#def add_int (a,b):
   # sum=a*b
   # return sum
#sum=add_int(7,7)

#print(sum)

#def avg_num (a,b,c):
 #   sum=a+b+c
  #  avg=sum/3
   # print(avg)
    #return avg
#avg_num(3,4,5)
##########

#print the len of a list(list is the parameter)

#cources = ("python","java","c++")
#university = ("cmr","reva","rv")

#def print_len(list):
 #   print(len(list))

#print_len(cources)
#print_len(university)

#print the elts of lit in a single line(list of parameter)
#def print_list(list):
  #  for item in list:
 #       print(item,end="")

#print_list(university)
#print()        


#factorial of n ( n is parameter)

#def fact_num(n):
 #   fact = 1
  #  for i in range(1,n+1):
   #     fact *=i
    #    print(fact)

#fact_num(8)      


#def converter(usd_val):
  #  inr_val=  usd_val * 83
 #   print (usd_val, "USD=", inr_val, "INR")

#converter(9)

#def check_even_odd(num):
    #if num % 2 == 0:
   #     print(f"{num} is Even.")
  #  else:
 #       print(f"{num} is Odd.")

# Example usage
#check_even_odd(91)

#def show(n):
    #if(n==0):
    #    return
  ## show(n-1)
 #   print("end")
    
#show(4)   


#def fact(n):
 #   if(n==1 or n==0):
  #      return 1
   # return fact(n-1) * n
#print(fact(4))

#def nat_sum(n):
   # if(n==0):
  #      return 0
 #   return nat_sum(n-1)+n

#sum=nat_sum(9)
#print(sum)

#def print_list(list,idx=0):
    #if(idx == len(list)):
   #     return
    
        
    
  #  print(list[idx])
 #   print_list(list, idx+1)
#names = ["dhanu","hemanth","chiranth","madan"]
#print_list(names)


#f=open("new.txt","r")
#line1=f.readline()
#print(line1)
#f.close()

#import os
#os.remove(dhanus.txt)

#class student:
   # def __init__(self,fullname):
  #      self.name=fullname
 #       print("adding student name")


#s1=student ("dhanush")
#print(s1.name)  

#s2=student ("madan")
#print(s2.name)      



class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc


    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"was debited") 
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"was credit") 
        print("total balance=",self.get_balance())    


    def get_balance(self):
        return self.balance


acc1=Account(10000,12345)
acc1.credit(1000)
acc1.debit(2500)
acc1.credit(1000)









#class Employee:
    #def __init__(self,dept,role,salary):
       # self.dept=dept
      #  self.role=role
     #   self.salary=salary

    #def showDetails(self):
   #     print("dept=",self.dept)
  #      print("salary=",self.salary)
 #       print("role=",self.role)

#class engneering(Employee):
    #def __init__(self,name,age):
   #      self.age=age 
 #       super().__init__("engineer","76000","it")       


#e1=engneering("Dhanush",23)
#e1.showDetails()   







    
     
    




    
    










    
        
    
 







   

    














 
       


