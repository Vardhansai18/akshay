import os

folders = [ 
    "noteboooks" , 
    "src" ,
    "saved_models" , 
    "data_given" ,
    "reports" ,
    "webapp" ,
    "prediction_service",
    os.path.join("webapp" , "static" ) ,
    os.path.join("webapp/static" , "css" ) ,
    os.path.join("webapp/static" , "script" ) ,

    os.path.join("data" , "raw" ) ,
    os.path.join("data" , "processed" ) 
   ]

files = [
    "dvc.yaml" , 
    "params.yaml" ,
    ".gitignore" ,
    os.path.join("prediction_service" , "model") ,  
    os.path.join("prediction_service" , "__init__.py") ,
    os.path.join("prediction_service" , "prediction.py") ,  
    os.path.join("webapp/static/css" , "main.css") , 
    os.path.join("webapp/static/script" , "index.js") , 
    os.path.join("reports" , "params.json") , 
    os.path.join("reports" , "scores.json") , 
    os.path.join("src" , "__init__.py") , 
    os.path.join("src" , "get_data.py") , 
    os.path.join("src" , "load_data.py") , 
    os.path.join("src" , "split_data.py") , 
    os.path.join("src" , "train_evaluate.py")  
]


for folder in folders:
    os.makedirs(folder , exist_ok = True )
    with open(os.path.join(folder,".gitkeep"),'w') as ss :
        pass


for f in files:
    with open(f,"w") as ff :
        pass
