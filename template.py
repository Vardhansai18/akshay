import os

folders = [ 
    "noteboooks" , 
    "src" ,
    "saved_models" , 
    "data_given" ,
    "reports" ,
    os.path.join("data" , "raw" ) ,
    os.path.join("data" , "processed" ) 
   ]

files = [
    "dvc.yaml" , 
    "params.yaml" ,
    ".gitignore" ,
    os.path.join("src" , "__init__.py") 
]


for folder in folders:
    os.makedirs(folder , exist_ok = True )
    with open(os.path.join(folder,".gitkeep"),'w') as ss :
        pass


for f in files:
    with open(f,"w") as ff :
        pass
