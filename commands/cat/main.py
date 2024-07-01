import argparse,os,sys 

parser = argparse.ArgumentParser()
parser.add_argument('filepath', action="store")
parser.add_argument('-n',action='store_true',default= False)
args = parser.parse_args()
print(args)
filepath = args.filepath
f=open(filepath,"r")
data=f.read()
splitedData=data.split("\n")
i=0
while i< len(splitedData):
    if(hasattr(args,'n')):
        print(i+1," ",splitedData[i])
    else:
        print(splitedData[i])
    i=i+1
f.close()