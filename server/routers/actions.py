from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response
import pandas as pd
import shutil
import json
from utils import heatmap
router = APIRouter()


@router.post('/uploadone')
async def upload_file(files:List = File(...)):
    # miRNA_data = pd.read_csv(files[0].file)
    # targets_data = pd.read_csv(files[1].file)
    # connections_data = pd.read_csv(files[2].file)
    # for file in files:
    #     file_location = f"{file.filename}"
    #     with open(file_location, "wb+") as file_object:
    #         shutil.copyfileobj(files[0].file, file_object)
    row_distance= str(files[1]).lower()
    row_linkage= str(files[2]).lower()
    try:
        respone_heatmap = heatmap.create_heatmap_json(files[0].filename,row_distance=row_distance,row_linkage=row_linkage)
        
        return respone_heatmap
    except Exception as e:
        print("error:",e)


  
@router.get('/upload2')
async def upload_file():
    row_distance= 'canberra'
    row_linkage= 'single'
    try:
        # respone_first_heatmap = heatmap.create_heatmap_json('input_file.csv',row_distance=row_distance,row_linkage=row_linkage)
        # respone_second_heatmap = heatmap.create_heatmap_json('example_data.csv',row_distance=row_distance,row_linkage=row_linkage)
        respone_first_heatmap = heatmap.create_heatmap_json('Mirim.csv',row_distance=row_distance,row_linkage=row_linkage)
        respone_second_heatmap = heatmap.create_heatmap_json('Geneim.csv',row_distance=row_distance,row_linkage=row_linkage)
        twomaps={ "first": respone_first_heatmap, "second": respone_second_heatmap };
        return twomaps;
    except Exception as e:
        print("error:",e)
  
