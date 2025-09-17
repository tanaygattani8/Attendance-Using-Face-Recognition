import os
from datetime import datetime

now = datetime.now()
date = now.strftime('%d-%m-%Y') 
with open(f'Attendence\{date}.csv' , 'r+') as t:
    read = t.readlines()
    print(read)
    lis = []
    for i in read:
        entry = i.split(',')
        print(entry[1])
        

    
        

