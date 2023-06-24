import os
index = []

for name in os.listdir():
    size = os.stat(name).st_size
    
    dict = {
    'Name': name, 
    'Size': size,
    }
    
    index.append(dict)
    
print(index, sep='\n')
