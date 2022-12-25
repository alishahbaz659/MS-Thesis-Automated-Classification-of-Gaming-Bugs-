import pandas as pd

from itertools import count
from lib2to3.pgen2.token import EQUAL


with open('reviews.jl', 'r',encoding="utf8") as f:
    lines = f.readlines()
    lines_length=len(lines)
with open('reviews.jl', 'w',encoding="utf8") as f:
    count=0
    for line in lines:
        count+=1
        if count != lines_length:
            f.writelines([line.strip(), ',\n'])
        else:
            f.writelines([line.strip()])
    
#Enclosing whole json to []
with open('reviews.jl', 'r',encoding="utf8") as f:
    reviews=f.read()
with open('reviews.jl', 'w',encoding="utf8") as f:
    f.write('['+reviews+']')   
        
        
#Converting JSON to CSV file
with open('reviews.jl', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)
df.to_csv('Reviews.csv', encoding='utf-8', index=False)