# ­*­ coding: utf­8 ­*­
import sys
from runge_kutt_adams import *
from math import *

def show_help():
  print('help --> show this message\n'
        'function= --> equation, argument x must be $x in input, y must be $y, function = y\'\n'        
        'interval=A%B --> interval of solving [A;B]\n'
        'condition=x%y, where x = x0, y = y(x0)\n'
        'answer= --> answer to equation, function y(x), x -> $x\n'
        'step=Z --> set step h\n'
        'graph=A --> where A is yes or y to make plot, other variants stop ploting')

def calculate(func, x):
  """calculate y=f(x)"""
  func = func.replace('$x', str(x))
  return eval(func)

exist_args = ['function', 'interval','condition', 'answer', 'step']
params = {'function' : '-($y * log($y))/x', 'interval' : '1%5', 'condition' : '1%2.72','answer' : 'e ** (1/$x)',
          'step' : '0.2', 'is_answer' : False, 'graph' : 'y'}


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
    if arg[0] == 'answer':
      params['is_answer'] = True

params['condition'] = params['condition'].split('%')
if len(params['condition']) != 2:
  print('Incorrect condition')
  exit(1)
params['interval'] = params['interval'].split('%')
if len(params['interval']) != 2:
  print('Incorrect interval')
  exit(2)
if params['interval'][0] > params['interval'][1] or params['condition'][0] < params['interval'][0] or params['condition'][0] > params['interval'][1]:
  print('Incorrect interval or condition')
  exit(3)

x0 = float(params['condition'][0])
y0 = float(params['condition'][1])  
h = float(params['step'])
a = float(params['interval'][0])
b = float(params['interval'][1])
if x0 > b or x0 < a:
  print('Incorrect interval or condition')
  exit(4)

answer = params['answer']

x_runge_1, y_runge_1 = [], []
x_runge_2, y_runge_2 = [], []
x_runge_3, y_runge_3 = [], []
x_runge_4, y_runge_4 = [], []
x_adams_1, y_adams_1 = [], []
x_adams_1, y_adams_2 = [], []
x_adams_1, y_adams_3 = [], []
x_runge_1, y_runge_1 = runge_kutt(params['function'],a,b,x0,y0,h,1)
x_runge_2, y_runge_2 = runge_kutt(params['function'],a,b,x0,y0,h,2)
x_runge_3, y_runge_3 = runge_kutt(params['function'],a,b,x0,y0,h,3)
x_runge_4, y_runge_4 = runge_kutt(params['function'],a,b,x0,y0,h,4)
x_adams_1, y_adams_1 = adams_bashfort(params['function'],a,b,x0,y0,h,1)
x_adams_2, y_adams_2 = adams_bashfort(params['function'],a,b,x0,y0,h,2)
x_adams_3, y_adams_3 = adams_bashfort(params['function'],a,b,x0,y0,h,3)

if params['graph'] == 'y' or params['graph'] == 'yes' and params['is_answer'] == True:
  
  answer = list(map(lambda a: calculate(params['answer'], a), x_runge_1))
  
  start_plot(x_runge_1, y_runge_1, x_runge_2, y_runge_2, x_runge_3, y_runge_3,
               x_runge_4, y_runge_4, x_adams_1, y_adams_1, x_adams_2, y_adams_2,
               x_adams_3, y_adams_3, answer, x_runge_1)
  
elif params['graph'] == 'y' or params['graph'] == 'yes' and params['is_answer'] != True:
  start_plot(x_runge_1, y_runge_1, x_runge_2, y_runge_2, x_runge_3, y_runge_3,
               x_runge_4, y_runge_4, x_adams_1, y_adams_1, x_adams_2, y_adams_2,
               x_adams_3, y_adams_3, ['no'], ['no'])
