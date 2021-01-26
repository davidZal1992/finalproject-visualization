from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response
import pandas as pd
import shutil
import json
import uuid
from utils import heatmap
import os


router = APIRouter()


@router.post('/uploadone')
async def upload_file(files:List = File(...)):
    if not os.path.exists('upload_data'):
        os.makedirs('upload_data')
    temp_files_array = []    
    temp_file = uuid.uuid4()
    file_location = f"upload_data/{temp_file}"
    print(file_location)
    temp_files_array.append(file_location)    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(files[0].file, file_object)
    row_distance= str(files[1]).lower()
    row_linkage= str(files[2]).lower()
    
    respone_heatmap = heatmap.create_heatmap_json(file_location,row_distance=row_distance,row_linkage=row_linkage)
        
    return respone_heatmap
    

@router.post('/upload')
async def upload_two_files(files:List = File(...)):
    if not os.path.exists('upload_data'):
        os.makedirs('upload_data')
    temp_files_array = []  
    index = 0   
    only_files=list(filter(lambda x: (type(x) is not str) ,files))
    for file in only_files:
        temp_file = uuid.uuid4()
        file_location = f"upload_data/{temp_file}"
        temp_files_array.append(file_location)
        print(type(file))
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        index=index+1    
    print(only_files)        
    row_distance= 'canberra'
    row_linkage= 'single'
    try:
        # respone_first_heatmap = heatmap.create_heatmap_json('Mirim.csv',row_distance=row_distance,row_linkage=row_linkage)
        # respone_second_heatmap = heatmap.create_heatmap_json('Geneim.csv',row_distance=row_distance,row_linkage=row_linkage)
        respone_first_heatmap = heatmap.create_heatmap_json(temp_files_array[0],row_distance=row_distance,row_linkage=row_linkage)
        respone_second_heatmap = heatmap.create_heatmap_json(temp_files_array[1],row_distance=row_distance,row_linkage=row_linkage)
        twomaps={ "first": respone_first_heatmap, "second": respone_second_heatmap };
        return twomaps;
    except Exception as e:
        print(e)
  
