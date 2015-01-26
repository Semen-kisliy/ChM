import csv
import pylab

def csv_input(file_name):
    infile = open(file_name, 'r')
    matrix = []
    b =[]

    for row in csv.reader(infile):
        matrix.append(row)
    infile.close()

    if len(matrix) > 0:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '':
                    matrix[r][c] = 0.0
                else:
                    matrix[r][c] =  float(matrix[r][c])
                
        for r in range(len(matrix)):
            b.append( matrix[r].pop() )
    else:
        print('Incorrect data in csv file!')
        exit (0)

    return matrix, b


def file_output(result,steps,time,accuracy,
                result2,steps2,time2,accuracy2,filename):
    i = 0
    if filename == 'CON':        
        for x in result:            
            print("MPI method")    
            print ('Answer: ',x)
            print ('Steps: ',steps[i])
            print ('Time: ',time[i])
            print ('Accuracy: ',accuracy[i],'\n')

            print("MNS method")
            print ('Answer: ',result2[i])
            print ('Steps: ',steps2[i])
            print ('Time: ',time2[i])
            print ('Accuracy: ',accuracy2[i],'\n')
            i += 1
            
    else:
        f = open(filename, "w")
        for x in result:
            f.write("MPI method\n")
            f.write (('Answer: %s' % x )+ '\n')
            f.write ('Steps: ' + str(steps[i])+ '\n')
            f.write (('Time: %.6s' % time[i]) +  '\n')
            f.write (('Accuracy: %.14f' % accuracy[i]) + '\n\n')

            f.write("MNS method\n")
            f.write (('Answer: %s' % result2[i]) + '\n')
            f.write ('Steps: ' + str (steps2[i]) + '\n')
            f.write (('Time: %.6f' % time2[i]) + '\n')
            f.write (('Accuracy: %.14f' % accuracy2[i]) + '\n\n')
            i += 1
            f.close()

def file_output_big(razmern,steps,time,accuracy,
                steps2,time2,accuracy2):
    fout = open('big.csv', 'w')
    fout.write('"Dim","MPI steps","MPI time","MNS steps","MNS time"\n')

    i = 0

    for x in razmern:
        fout.write (str(x) + ',' + str(steps[i])+ ',' + ("%.6f" % time[i]) +
              ',' + str(steps2[i]) +',' + ("%.6f" %time2[i]) + '\n')
        i += 1 
    fout.close()
        

def start_plot(steps,time,
               steps2,time2,razmern):
    pylab.subplot(2,1,1)
    pylab.plot (razmern, steps,  "b")
    pylab.plot (razmern, steps2, "g")
    pylab.legend (["mpi","mns"])
    pylab.ylabel('steps')
    pylab.xlabel('dimention')
    pylab.grid(True)
    pylab.subplot(2,1,2)
    pylab.plot (razmern,time, "b")
    pylab.plot (razmern,time2, "g")
    pylab.legend (["mpi","mns"])
    pylab.ylabel('Time')
    pylab.xlabel('dimention')
    pylab.grid(True)
    
    pylab.show()
