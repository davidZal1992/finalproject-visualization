from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response
import pandas as pd
import shutil
import json
from utils import heatmap
router = APIRouter()




@router.post('/upload')
async def upload_file(files: List[UploadFile] = File(...)):
    # miRNA_data = pd.read_csv(files[0].file)
    # targets_data = pd.read_csv(files[1].file)
    # connections_data = pd.read_csv(files[2].file)
    for file in files:
        file_location = f"{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(files[0].file, file_object)
    a = [x.filename for x in files]
    try:
        respone_heatmap = heatmap.create_heatmap_json(files[0].filename)
        print(respone_heatmap)
        return respone_heatmap
    except Exception as e:
        print(e)








@router.get('/upload2')
def upload_file2():
    print('success')
    return {"hello": "world"}
  

