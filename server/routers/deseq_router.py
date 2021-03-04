from fastapi import APIRouter,Header,HTTPException,FastAPI, File,Response,Request
from fastapi.responses import HTMLResponse
import json
import os
from typing import List
import shutil
from controller import deseq_controller

router = APIRouter()

@router.post('/run_deseq')
async def run_deseq(request :Request):
    data = await request.form()
    deseq_result =  deseq_controller.run_deseq_controller(data)
    return {'deseq_results':deseq_result}

@router.post('/volcano_plot_deseq',response_class=HTMLResponse)
async def deseq_volcano(request :Request):
    data = await request.form()
    fig_json = deseq_controller.deseq_volcano_controller(data)
    return fig_json

@router.post('/upload_data')
async def upload_data(files:List = File(...)):
    for file in files:
        file_name = file.filename
        with open(file_name, "wb+") as file_object:
            file_object.write(file.file.read())
            file_object.close()
    return {"message": "The files were saved to the server successfully."}


@router.get('/get_files')
async def get_files_names(request: Request):
    files=[]
    for file in os.walk(r"C:\Users\gal\Desktop\ISE\project\data\csv"):
        files.append(file[2])
    return {"files": files}

# @router.get('/download/{path}')
# async def download_file(request :Request):
#     file_path = request.query_params['path']
#     with open(file_path,"rb") as file:
#         bytes =await file.read()




