def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a>0 and b>0:
      if a>=b:
          a=a%b
      else:
          b=b%a
  return max(a,b)

         

def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  def extended_gcd(a,b):
      assert a>=0 and b>=0 and a+b>0
      if b==0:
          d,x,y=a,1,0
      else:
          (d,p,q)=extended_gcd(b,a%b)
          x=q
          y=p-q*(a//b)
      assert a%d==0 and b%d==0
      assert d==a*x+b*y
      return (d,x,y)
  d,x,y=extended_gcd(a,b)
  t=c/d
  assert c==a*t*x+b*t*y
  return (t*x,t*y)
print (diophantine(4,5,20))