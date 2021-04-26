import pandas as pd

def marking(file):
    df=pd.read_csv(file)
    infile=open('class_progress.txt','w')
    col=[]
    for i in df:
        col.append(i)
    presents=[]
    absents=[]
    for i in range(len(df[col[1]])):
        if df.loc[i,col[1]]=='a':
            absents.append(df.loc[i,col[0]])
        else:
            presents.append(df.loc[i,col[0]])
    infile.write('\n*****PRESENT STUDENTS*****\n')
    for i in presents:
        infile.write('\n{}'.format(i))
    infile.write('\n*****ABSENTS STUDENTS*****\n')
    for x in absents:
        infile.write('\n{}'.format(x))
    infile.close()
marking('example.csv')