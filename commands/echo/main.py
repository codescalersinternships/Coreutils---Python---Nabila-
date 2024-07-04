import os,argparse

parser = argparse.ArgumentParser()
parser.add_argument('toPrint', action="extend", nargs="+", type=str)
parser.add_argument('-n',action='store_true',default= False)
args = parser.parse_args()

showNewLine=args.n
tobePrinted=args.toPrint

# print(" ".join(tobePrinted), end="")
for word in tobePrinted:
    print(word, " ", end="")
if(not showNewLine):
    print()