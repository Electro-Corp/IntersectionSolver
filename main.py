m1 = int(input("M1: "))
c1 = int(input ("c1: "))
m2 = int(input ("M2: "))
c2 = int(input ("c2: "))
def FindIntersection(m1,c1,m2,c2):
  side1 = m1-m2
  sid2 = c2-c1
  print(side1)
  print(sid2)
  x = sid2/side1
  y = (m1*x) +c1
  print("Intersect at: (", x,",",y,")")
print("Equation 1: ", "y = ", m1,"x + ",c1)
print("Equation 2: ", "y = ", m2,"x + ",c2)
FindIntersection(m1,c1,m2,c2)
