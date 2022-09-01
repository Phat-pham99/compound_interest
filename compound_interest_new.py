def com_int(P : int,n : int,r :float,t:int) :
       A = P*((1+r/n)**(n*t))
       A = int(A)
       aa = A
       P1 = '{0:,}'.format(P)
       aa1 = '{0:,}'.format(aa)
       bb = aa - P
       bb1 = '{0:,}'.format(bb)
       cc = P*r*t
       cc = int(cc)
       cc1 = '{0:,}'.format(cc)
       dd = bb/cc*100
       dd = round(dd,2)
       dd1 = '{0:,}'.format(dd)
       print("+----------------------------+")
       print("Initial Principle {}".format(str(P1)))
       print("Total {} ".format(str(aa1)))
       print("Compound Interest {} ".format(str(bb1)))
       print(">---<")
       print("Simple Interest {}".format(str(cc1)))
       print("CI/SI percentage {}".format(str(dd1)))
       print("+------------------------------+")
       return A 

def each_month(init : int,P : int,r : float,t : int):
       # P : the principle amount you invest each month
       # r : Interest per year
       # t : number of months
       print("+------------------------------+")
       result = init
       for i in range(1,t+1):
              result = (result+P)*(1+r/12)
              result = int(result)
              result1 = '{0:,}'.format(result)
              print(" +  Month #{}| {}     ".format(i,result1))
       print("+------------------------------+")
       basse = init + P * t
       diff = result - basse
       #result = '{0:,}'.format(result)
       basse1 = '{0:,}'.format(basse)
       diff1 = '{0:,}'.format(diff)
       print(" Total if CI : {}".format(result1))
       print(" Total if stack : {}".format(basse1))
       print(" The difference is {}".format(diff1))
       print("+------------------------------+")
       return result

# Common part
print("If you want to calculate compound interest from initial Principle, press 1")
print("If you want to calculate CI on investment each month, press 2")
index = input("Here : ")
P = input("Investment each month : ")
P = eval(P)
P = int(P)
init = input("Initial Principle : ")
init = float(init)
r = input("Interest rate : ")
r = eval(r)
r = float(r)
n = 365
t = input("Time of investment : ")
t = eval(t)
t = int(t)
#########################
total = 0
if index == "1" : 
       total = com_int(P,n,r,t)

elif index =="2" :
       total = each_month(init,P,r,t)
       print("Do you want to keep investing ?")
       jj = input("Press y or n :      ")
       print("+------------------------------+")
       if jj =="y" :
              #########################
              P1 = input("Investment each month : ")
              P1 = eval(P1)
              P1 = int(P1)
              r1 = input("Interest rate : ")
              r1 = eval(r1)
              r1 = float(r1)
              t1 = input("Time of investment : ")
              t1 = eval(t1)
              t1 = int(t1)
              #########################
              later = each_month(total,P1,r1,t1)
       else :
              pass
else :
  print(" +------------------------------+ ")
  print("The fuck man ?")
