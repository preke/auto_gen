import os
import time
import re
import traceback

'''
Combine all the remainders and their corresponding paper number into one file
'''

pattern = re.compile(r'\d+') 
path = "remainder"
files= os.listdir(path)
with open('remainder_data.txt', 'w') as fw:
    for file in files:
        if not os.path.isdir(file) and file[-4:] == '.txt':
            paper_num = pattern.findall(file)[0]
            print(paper_num)
            try:
                f = open(path+"/"+file)
                iter_f = iter(f)
                str_ = ""
                for line in iter_f:
                    str_ = str_ + line
                fw.write(paper_num + '\t' + str_ + '\n')
            except:
                print(file)
                print(traceback.print_exc())


