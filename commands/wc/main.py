import argparse,os,sys 

parser = argparse.ArgumentParser()
parser.add_argument('filepath', action="store")
parser.add_argument('-l',action='store_true',default= False)
parser.add_argument('-w', action='store_true',default=False)
parser.add_argument('-c', action='store_true',default=False)

args = parser.parse_args()
filepath = args.filepath
f=open(filepath,"r")
data=f.read()
splitedData=data.split("\n")

showLines=args.l
showWords=args.w
showCharacters=args.c

if showLines or (not showLines and not showWords and not showCharacters):
    print(len(splitedData))
if showWords or (not showLines and not showWords and not showCharacters):
    print(len(data.split()))
if showCharacters or (not showLines and not showWords and not showCharacters):
    print(len(data))
f.close()

