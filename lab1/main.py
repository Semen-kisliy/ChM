import numpy as np
from files import *
from vec_and_matr import *
from MPI import *
from MNS import *
import time as t
import sys

def show_help():
  print('help --> show this message\n'
        'mode=A --> where A is TEST or FILE or BIG,when selected FILE, please enter filename in intput\'\n'
        'output=B --> where B is name of the output file or CON,output to console\n'
        'eps=C --> where C is precision of dimensions\n'
        'input=D --> where D is name of file with data,when selected FILE mode\n'
        'graph=E --> where E is yes or y to take plot\n')

exist_args = ['mode', 'output', 'eps', 'input']
params = {'mode' : 'FILE', 'output' : 'CON', 'eps' : '1e-8', 'input': 'in2.csv', 'graph' : 'y'}


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
    if arg[0] == 'TEST':
      params['input'] = 'None'



eps = float(params['eps'])
outputfile = params['output']

result_mns = []
result_mpi = []
steps_mns = []
steps_mpi = [] 
accuracy_mns = []
accuracy_mpi = []
time_mns = []
time_mpi = []

if params['mode'] == 'TEST':
    
    razmer = [c for c in range(3,14)]
    for i in razmer:
        A = matrix_generate(i)
        b = vector_b_generate(i)

        t1 = t.clock()
        res,step,acc = MNS(A,b,eps)
        t2 = t.clock()

        time_mns.append(t2-t1)
        result_mns.append(res)
        steps_mns.append(step)
        accuracy_mns.append(acc)

        t1 = t.clock()
        res,step,acc = MPI(A,b,eps)
        t2 = t.clock()

        time_mpi.append(t2-t1)
        result_mpi.append(res)
        steps_mpi.append(step)
        accuracy_mpi.append(acc)
        
        
    
    file_output(result_mpi,steps_mpi,time_mpi,accuracy_mpi,
                result_mns,steps_mns,time_mns,accuracy_mns,params['output'])

    if params['graph'] == 'yes' or  params['graph'] == 'y':
      start_plot(steps_mpi,time_mpi,steps_mns,time_mns,razmer)

    
elif params['mode'] == 'FILE':
  
    A,b = csv_input(params['input'])
    if determinant(A) == 0:
      print('Determinant of matrix A = 0')
    else:
      if check_square(A):
        if not check_simmetric(A) or not check_positive(A):
          AT = trance(A)
          A = np.dot(AT,A)

          b = np.dot(AT,b)

        t1 = t.clock()
        res,step,acc = MNS(A,b,eps)
        t2 = t.clock()

        time_mns.append(t2-t1)
        result_mns.append(res)
        steps_mns.append(step)
        accuracy_mns.append(acc)

        t1 = t.clock()
        res,step,acc = MPI(A,b,eps)
        t2 = t.clock()

        time_mpi.append(t2-t1)
        result_mpi.append(res)
        steps_mpi.append(step)
        accuracy_mpi.append(acc)

        
        file_output(result_mpi,steps_mpi,time_mpi,accuracy_mpi,
                result_mns,steps_mns,time_mns,accuracy_mns,params['output'])
      else:
        print('Matrix A not square')
        
elif params['mode'] == 'BIG':
  razmer = [150,300,500,750,1000,1500]
  for i in razmer:
    A = matrix_generate(i)
    b = vector_b_generate(i)

    t1 = t.clock()
    res,step,acc = MNS(A,b,eps)
    t2 = t.clock()

    time_mns.append(t2-t1)
    steps_mns.append(step)
    accuracy_mns.append(acc)

    t1 = t.clock()
    res,step,acc = MPI(A,b,eps)
    t2 = t.clock()

    time_mpi.append(t2-t1)
    steps_mpi.append(step)
    accuracy_mpi.append(acc)

  if params['graph'] == 'yes' or  params['graph'] == 'y':
      start_plot(steps_mpi,time_mpi,steps_mns,time_mns,razmer)

  file_output_big(razmer,steps_mpi,time_mpi,accuracy_mpi,steps_mns,time_mns,accuracy_mns)
