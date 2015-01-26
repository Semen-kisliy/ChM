# ­*­ coding: utf­8 ­*­
from math import *
import sys
import pylab

def calculate(func, x, y):
  func = func.replace('$x', str(x))
  func = func.replace('$y', str(y))
  return eval(func)

def runge_next_point(func, x, y, h, rank):
  k1 = calculate(func, x, y) #k1 == dy when rank == 1
  if rank == 1:    
    y +=  h*k1
    return y
  elif rank == 2:
    k2 = calculate(func, (x + 2*h/3), (y + 2 * h * k1/3) )
    y += h*(k1+3*k2)/4
    return y
  elif rank == 3:
    k2 = calculate(func, (x + h/2), (y + h * k1 /2) )
    k3 = calculate(func, (x + h), (y - h * k1 + 2 * h * k2) )
    y += h*(k1+4*k2+k3)/6
    return y
  elif rank == 4:
    k2 = calculate(func, (x + h/2), (y + h * k1 / 2) )
    k3 = calculate(func, (x + h/2), (y + h * k2 / 2) )
    k4 = calculate(func, (x + h), (y + h * k3) )
    y += h*(k1 + 2*k2 + 2*k3 + k4)/6
    return y
  

def runge_previous_point(func, x, y, h, rank):
  k1 = calculate(func, x, y) #k1 == dy when rank == 1
  if rank == 1:    
    y -=  h*k1
    return y
  elif rank == 2:
    k2 = calculate(func, (x - 2*h/3), (y - 2 * h* k1/3) )
    y -= h*(k1+3*k2)/4
    return y
  elif rank == 3:
    k2 = calculate(func, (x - h/2), (y - h * k1 / 2) )
    k3 = calculate(func, (x - h), (y + h * k1 - 2* h *k2) )
    y -= h*(k1+4*k2+k3)/6
    return y
  elif rank == 4:
    k2 = calculate(func, (x - h/2), (y - h * k1 / 2) )
    k3 = calculate(func, (x - h/2), (y - h * k2 / 2) )
    k4 = calculate(func, (x - h), (y - h * k3) )
    y -= h*(k1 + 2*k2 + 2*k3 + k4)/6
    return y

  
def runge_kutt(func, a , b, x0, y0, h, rank):
  eps = 1e-6
  y_list = []
  x_list = []
  x_list_half_h = []
  y_list_half_h = []
  
  x_list.append(x0)
  y_list.append(y0)

  x_list_half_h.append(x0)
  y_list_half_h.append(y0)

  while x_list[-1] - h > a + eps:
    yi = runge_previous_point(func, x_list[-1], y_list[-1], h, rank)
    x_list.append(x_list[-1] - h)
    y_list.append( yi )

    # calc R
    yi2 = runge_previous_point(func, x_list_half_h[-1], y_list_half_h[-1], (h/2), rank)
    x_list_half_h.append(x_list_half_h[-1] - (h/2))
    y_list_half_h.append( yi2 )
    yi2 = runge_previous_point(func, x_list_half_h[-1], y_list_half_h[-1], (h/2), rank)
    x_list_half_h.append(x_list_half_h[-1] - (h/2))
    y_list_half_h.append( yi2 )

    R =  (y_list_half_h[-1] - y_list[-1]) / (2**rank -1)

    
  x_list = x_list[:0:-1]
  y_list = y_list[:0:-1]
  
  x_list.append(x0)
  y_list.append(y0)

  x_list_half_h[:0:]
  y_list_half_h[:0:]
  x_list_half_h.append(x0)
  y_list_half_h.append(y0)

  while x_list[-1] + h < b - eps:
    yi = runge_next_point(func, x_list[-1], y_list[-1], h, rank)
    x_list.append(x_list[-1] + h)
    y_list.append( yi )

    # calc R
    yi2 = runge_previous_point(func, x_list_half_h[-1], y_list_half_h[-1], (h/2), rank)
    x_list_half_h.append(x_list_half_h[-1] + (h/2))
    y_list_half_h.append( yi2 )
    yi2 = runge_previous_point(func, x_list_half_h[-1], y_list_half_h[-1], (h/2), rank)
    x_list_half_h.append(x_list_half_h[-1] + (h/2))
    y_list_half_h.append( yi2 )

    R =  (y_list_half_h[-1] - y_list[-1]) / (2**rank -1)
    
  return  x_list, y_list
  

def adams_bashfort(func, a , b, x0, y0, h, rank):
  eps = 1e-6
  y_list = []
  x_list = []
  x_list.append(x0)
  y_list.append(y0)


  if rank == 1:     
    while x_list[-1] - h > a + eps:
      dy = h*calculate(func, x_list[-1], y_list[-1]) # dy when rank == 1
      y_list.append(y_list[-1] - dy)
      x_list.append(x_list[-1] - h)
      
    x_list = x_list[:0:-1]
    y_list = y_list[:0:-1]

    x_list.append(x0)
    y_list.append(y0)

    while x_list[-1] + h < b - eps:
      dy = h*calculate(func, x_list[-1], y_list[-1]) # dy when rank == 1
      y_list.append(y_list[-1] + dy)
      x_list.append(x_list[-1] + h)

     
  elif rank == 2:   
    if (x_list[-1] + h > b - eps):
        print('Метод Адамса (2).Невозможно вычислить значение для точки 2 в x = ',x_list[-1] + h )
        x_list.append( x_list[-1] - h )
        y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) ) 
    else:
        x_list.append( x_list[-1] + h )
        y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
        x_list = x_list[::-1]
        y_list = y_list[::-1]
        
    
    while x_list[-1] - h > a + eps:
      dy = (h/2)*(3*calculate(func, x_list[-1],y_list[-1]) - calculate(func, x_list[-2],y_list[-2]))
      y_list.append(y_list[-1] - dy)
      x_list.append(x_list[-1] - h)
  
      
    if x_list.index(x0) == 0:
      x_list = x_list[:0:-1]
      y_list = y_list[:0:-1]
      x_list.append(x0)
      y_list.append(y0)
    else:
      x_list = x_list[:1:-1]
      y_list = y_list[:1:-1]
      x_list.append(x0)
      y_list.append(y0)   

   
    if (x_list[-1] - h < a + eps):
        print('Метод Адамса (2).Невозможно вычислить значение для точки 2 в x = ',x_list[-1] - h )
        x_list.append( x_list[-1] + h )
        y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) ) 
    elif (x_list[-1] - h > a + eps) and (x_list[-1] - h not in x_list):
        x_list.append( x_list[-1] - h )        
        y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )
        x_list = x_list[::-1]
        y_list = y_list[::-1]

        
    while x_list[-1] + h < b - eps:
      dy = (h/2)*(3*calculate(func, x_list[-1],y_list[-1]) - calculate(func, x_list[-2],y_list[-2]))
      y_list.append(y_list[-1] + dy)
      x_list.append(x_list[-1] + h)

   
  elif rank == 3:    
    if (x_list[-1] + h > b - eps):
      print('Метод Адамса (3).Невозможно вычислить значение для точки 2 в x = ',x_list[-1] + h )
      x_list.append( x_list[-1] - h )
      y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )
      x_list.append( x_list[-1] - h )
      y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )        
    else:
      x_list.append( x_list[-1] + h )
      y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
      if (x_list[-1] + h > b - eps):
        print('Метод Адамса (3).Невозможно вычислить значение для точки 3 в x = ',x_list[-1] + h )
        x_list = x_list[::-1]
        y_list = y_list[::-1]
        x_list.append( x_list[-1] - 2*h )
        y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )
      else:
        x_list.append( x_list[-1] + h )
        y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
        x_list = x_list[::-1]
        y_list = y_list[::-1]
          
    while x_list[-1] - h > a + eps:  #FIRST WHILE *************************
      dy = (h/12)*(23*calculate(func, x_list[-1],y_list[-1])
                - 16*calculate(func, x_list[-2],y_list[-2])
                 + 5*calculate(func, x_list[-3],y_list[-3]))
      y_list.append(y_list[-1] - dy)
      x_list.append(x_list[-1] - h)
      

    if x_list.index(x0) == 0:
      x_list = x_list[:0:-1]
      y_list = y_list[:0:-1]
      x_list.append(x0)
      y_list.append(y0)
    elif x_list.index(x0) == 1:
      x_list = x_list[:1:-1]
      y_list = y_list[:1:-1]
      x_list.append(x0)
      y_list.append(y0)
    elif x_list.index(x0) == 2:
      x_list = x_list[:2:-1]
      y_list = y_list[:2:-1]
      x_list.append(x0)
      y_list.append(y0)

    if (x_list[-1] - h < a + eps):
      print('Метод Адамса (3).Невозможно вычислить значение для точки 2 в x = ',x_list[-1] - h )
      x_list.append( x_list[-1] + h )
      y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
      x_list.append( x_list[-1] + h )
      y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
    elif (x_list[-1] - h > a + eps) and (x_list[-1] - h not in x_list):
      x_list.append( x_list[-1] - h )
      y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )
      if (x_list[-1] - h < a + eps):
        print('Метод Адамса (3).Невозможно вычислить значение для точки 2 в x = ',x_list[-1] - h )
        x_list = x_list[::-1]
        y_list = y_list[::-1]
        x_list.append( x_list[-1] + 2*h )
        y_list.append( y_list[-1] + h*calculate(func, x_list[-1], y_list[-1]) )
      elif (x_list[-1] - h > a + eps) and (x_list[-1] - h not in x_list):
        x_list.append( x_list[-1] - h )
        y_list.append( y_list[-1] - h*calculate(func, x_list[-1], y_list[-1]) )
        x_list = x_list[::-1]
        y_list = y_list[::-1]


    while x_list[-1] + h < b - eps:  # Second WHILE ********************
      dy = (h/12)*(23*calculate(func, x_list[-1],y_list[-1])
                - 16*calculate(func, x_list[-2],y_list[-2])
                 + 5*calculate(func, x_list[-3],y_list[-3]))
      y_list.append(y_list[-1] + dy)
      x_list.append(x_list[-1] + h)
  
  return x_list, y_list


def start_plot(x_runge_1, y_runge_1, x_runge_2, y_runge_2, x_runge_3, y_runge_3,
               x_runge_4, y_runge_4, x_adams_1, y_adams_1, x_adams_2, y_adams_2,
               x_adams_3, y_adams_3, is_answer_y, is_answer_x):
  pylab.subplot(2,4,1)
  pylab.plot (x_runge_1, y_runge_1, "b")
  pylab.ylabel('function(runge-kutt 1)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,2)
  pylab.plot (x_runge_2, y_runge_2, "b")
  pylab.ylabel('function(runge-kutt 2)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,3)
  pylab.plot (x_runge_3, y_runge_3, "b")
  pylab.ylabel('function(runge-kutt 3)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,4)
  pylab.plot (x_runge_4, y_runge_4, "b")
  pylab.ylabel('function(runge-kutt 4)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,5)
  pylab.plot (x_adams_1, y_adams_1, "y")
  pylab.ylabel('function(adams 1)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,6)
  pylab.plot (x_adams_2, y_adams_2, "y")
  pylab.ylabel('function(adams 2)')
  pylab.xlabel('points')
  pylab.grid(True)

  pylab.subplot(2,4,7)
  pylab.plot (x_adams_3, y_adams_3, "y")
  pylab.ylabel('function(adams 3)')
  pylab.xlabel('points')
  pylab.grid(True)
  
  if is_answer_y[0] != 'no' and is_answer_x[0] != 'no':
    pylab.subplot(2,4,8)
    pylab.plot (is_answer_y, is_answer_x, "g--")
    pylab.plot (x_runge_4, y_runge_4, "b-.")
    pylab.plot (x_adams_3, y_adams_3, "r+")
    pylab.ylabel('function')
    pylab.xlabel('points')
    pylab.legend(["real", "runge-kutt", "adams"])
    pylab.grid(True)

  pylab.show()
