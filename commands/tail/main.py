import argparse,os,sys 

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, default=10)
parser.add_argument('filepath', action="store")

args = parser.parse_args()
filepath = args.filepath
n = args.n 
f=open(filepath,"r")
data=f.read()
splitedData=data.split("\n")
i=len(splitedData)-1
j=0
while i>=0 and j < len(splitedData) and j<=n:
    print(splitedData[i])
    i=i-1
    j=j+1
f.close()

