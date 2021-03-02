import pandas as pd
import os
import sys



'getcwd:      ', os.getcwd()
osfile, maindir =('__file__:    ', __file__)
filename = os.path.basename(sys.argv[0])
inpath = maindir.replace(filename,"Excels")
outpath = maindir.replace(filename,"BulkFile.xlsx")




#########pandas script
def read_xl_dir():
    for root, dirs, files in os.walk(inpath):
        for f in files:
            filepath = os.path.join(root, f)
            name, extension = os.path.splitext(filepath)
            if extension == '.xlsx':
                print(filepath)









read_xl_dir()