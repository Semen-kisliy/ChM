# ­*­ coding: utf­8 ­*­
import math
from math import *
import sys
import quadrature_methods as qm

def show_help():
  print('help --> show this message\n'
        'function=\'~~~\' --> function for integration, argument x must be $x in input\n'
        'interval=A%B --> interval of integration [A;B]\n'
        'plot=A --> y or yes - enable charts, n or other combination - disable\n'
        'chart=TYPE --> set chart type: TIME or AMOUNT or BOTH')

exist_args = ['function',  'interval', 'plot', 'chart']
params = {'function' : '$x', 'interval' : '0%1', 'plot' : 'y', 'chart' : 'AMOUNT'}

for raw_arg in sys.argv:
  if raw_arg == sys.argv[0]:
    continue
  if raw_arg == 'help':
    show_help()
    exit(0)
  arg = raw_arg.split('=')
  if len(arg) != 2 or arg[0] not in exist_args:
    print('Incorrect parameter \'' + raw_arg + '\'')
  else:
    params[arg[0]] = arg[1]


params['interval'] = params['interval'].split('%')
if len(params['interval']) != 2:
  print('Incorrect interval')
  exit(1)
a = float(params['interval'][0])
b = float(params['interval'][1])
if a > b:
  a, b = b, a


left, right, time = 0.0, 0.0, 0.0
left_list, right_list, left_time, right_time, r_list, delta = [], [], [], [], [], []
points_amount = [100,150,200,250,300,350,400,450,500,550,600]

for i in points_amount:
    left, time = qm.rectangle_left(params['function'],a,b,i)
    left_list.append(left)
    left_time.append(time)
    right, time = qm.rectangle_right(params['function'],a,b,i)
    right_list.append(right)    
    right_time.append(time)    
    r_list.append(qm.infelicity(params['function'],a,b,i))
    delta.append(qm.delta(left,right))
    
print('\nleft integral: ',left_list[points_amount.index(600)])
print('right integral: ',right_list[points_amount.index(600)])
print ('R is: ',r_list[points_amount.index(600)])

if params['plot'] == 'y' or params['plot'] == 'yes':
    if params['chart'] == 'BOTH':
        qm.start_plot_both(points_amount,left_list,right_list,left_time,right_time)
    elif params['chart'] == 'TIME':
        qm.start_plot_time(points_amount,left_time,right_time)
    elif params['chart'] == 'AMOUNT':
        qm.start_plot_amount(points_amount,left_list,right_list)
    else:
      print ('Incorrect parameter chart\n')
      exit(1)
