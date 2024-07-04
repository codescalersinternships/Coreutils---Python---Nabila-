import argparse,os,sys 

def printDirectory (directoryPath, depth,currentDepth):
    if(depth==currentDepth):
        return
    for currentLocation in os.listdir(directoryPath):
        i=0
        while(i<currentDepth):
            print("   ",end="")
            i=i+1
        print("|―",currentLocation)
        path=os.path.join(directoryPath,currentLocation)
        if(os.path.isdir(path)):
            printDirectory(path,depth,currentDepth+1)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-L', type=int, default=1)
    parser.add_argument('directorypath', action="store")
    args = parser.parse_args()
    print(args)
    directoryPath = args.directorypath
    depth = args.L
    printDirectory(directoryPath, depth, 0)

main()