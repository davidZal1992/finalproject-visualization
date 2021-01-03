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
    for file in files:
        temp_file = uuid.uuid4()
        file_location = f"upload_data/{temp_file}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(files[0].file, file_object)
    row_distance= str(files[1]).lower()
    row_linkage= str(files[2]).lower()
    
    respone_heatmap = heatmap.create_heatmap_json(files[0].filename,row_distance=row_distance,row_linkage=row_linkage)
        
    return respone_heatmap
    








@router.get('/upload2')
def upload_file2():
    print('success')
    return {"hello": "world"}
  

