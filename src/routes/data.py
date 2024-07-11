from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from controllers import DataController, ProjectController
from helpers.config import get_settings, Settings
from fastapi.responses import JSONResponse
from models import ResponseSignal
import aiofiles
import logging
from .schemes.data import ProcessRequest


logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags= ["api_v1","data"]
)


@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    
    data_controller = DataController()
    
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
        
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name= file.filename , project_id=project_id
        )
    
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    return JSONResponse(
            content={
                "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )
    

@data_router.post("/process/{project_id}")
async def process_endpoint(project_id: str,process_request: ProcessRequest):
    
    file_id = process_request.file_id
    
    return file_id