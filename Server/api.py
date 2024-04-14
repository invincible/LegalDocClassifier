from fastapi import FastAPI, File, UploadFile
from typing import List
import shutil
import os

from main import check_type, get_files, upload_files

app = FastAPI()

@app.post("/classify")
def type(file: UploadFile = File(...)):
    if not os.path.exists("uploaded_files"):
        os.makedirs("uploaded_files")
    try:
        with open(f"uploaded_files/{file.filename}", "wb") as f:
            #shutil.copyfileobj(file.file, f)
            f.write(file.file.read())
    except Exception:
        return {"message": "There was an error uploading the file(s)"}
    finally:
        file.file.close()

    return {"file_name": file.filename, "document_type": check_type(f"uploaded_files/{file.filename}")}

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    if not os.path.exists("uploaded_files"):
        os.makedirs("uploaded_files")
    result = {"data": []}
    for file in files:
        try:
            with open(f"uploaded_files/{file.filename}", "wb") as f:
                shutil.copyfileobj(file.file, f)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

        result["data"].append({"filename": file.filename, "document_type": upload_files(f"uploaded_files/{file.filename}")})

    return result

@app.get("/files")
def files():
    return get_files()