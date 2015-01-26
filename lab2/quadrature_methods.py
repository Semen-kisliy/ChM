# ­*­ coding: utf­8 ­*­
import math
import time
#import matplotlib as mplot
import pylab

def compute(func, x):
  func = func.replace('$x', str(x))
  return eval(func)

def delta(I1, I2):
  return (abs(I1 - I2)/2)

def rectangle_left(function, a, b, n):
    t1 = time.clock() 
    I_left = 0.0
    h = (b - a)/n
    x_list = []
    x_list.insert(0,a)
    i = 1
    
    while i <= n - 2:
        x_list.append(x_list[i - 1] + h)
        i += 1
    x_list.insert(n-1,b)
    
    for i in range(n-1):
        I_left += compute(function,x_list[i])
    I_left *= h
    
    t2 = time.clock()
    return I_left, (t2 -t1)

def rectangle_right(function, a, b, n):
    t1 = time.clock() 
    I_right = 0.0
    h = (b - a)/n
    x_list = []
    x_list.insert(0,a)
    i = 1
    
    while i <= n - 2:
        x_list.append(x_list[i - 1] + h)
        i += 1
    x_list.insert(n-1,b)
    
    for i in range(1,n):
        I_right += compute(function,x_list[i])
    I_right *= h
    
    t2 = time.clock()
    return I_right, (t2 -t1)

def infelicity(function, a, b, n):
  list_of_fx = []
  eps = (b - a)/n
  fx = compute(function,a + eps)
  dx = eps 
  i = a + 2*eps
  x = a + eps
  while i < b:
    intermediate = compute(function,i)
    if fx < intermediate:
      fx = compute(function,i)
      x = i 
    i += eps
      
  fxdx = compute(function,(x+dx))
  fx2dx = compute(function,(x+2*dx))
  R = ((fx2dx - 2*fxdx + fx)*(b - a)*(eps**2))/((dx**2) * 24)

  return abs(R)


def start_plot_amount(x, y, y1):
  pylab.plot (x, y, "r")
  pylab.plot (x, y1, "b")
  pylab.xlabel('points')
  pylab.ylabel('integral')
  pylab.legend (["left integral", "right integral"])
  pylab.grid(True)
  pylab.show()

def start_plot_time(x, y, y1):
  pylab.plot (x, y, "r")
  pylab.plot (x, y1, "b")
  pylab.xlabel('time')
  pylab.ylabel('integral')
  pylab.legend (["left integral", "right integral"])
  pylab.grid(True)
  pylab.show()


def start_plot_both(x, y, y1, y2 ,y3):
  pylab.subplot(2,2,1)
  pylab.plot (x, y, "r")
  pylab.ylabel('integral')
  pylab.legend (["left integral"])
  pylab.grid(True)
  pylab.subplot(2,2,2)
  pylab.plot (x, y1, "b")
  pylab.legend (["right integral"])
  pylab.grid(True)
  pylab.subplot(2,2,3)
  pylab.plot (x, y3, "y")
  pylab.xlabel('points')
  pylab.ylabel('time')
  pylab.legend (["left integral"])
  pylab.grid(True)
  pylab.subplot(2,2,4)
  pylab.plot (x, y3, "g")
  pylab.xlabel('points')
  pylab.legend (["right integral"])
  pylab.grid(True)
  pylab.show()
