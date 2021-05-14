import io
import numpy as np
from fastapi import FastAPI, Response, File, UploadFile
from rembg.bg import remove
from PIL import Image

app = FastAPI()

default_path = 'nobg.png'

async def remove_background(file: UploadFile = File(...)):
    f_content = await file.read()
    f = np.frombuffer(f_content, np.uint8)
    nobg_buff = remove(f)
    nobg_image = Image.open(io.BytesIO(nobg_buff)).convert("RGBA")
    filename = f'{file.filename}-nobg.png'
    nobg_image.save(filename)
    return nobg_image.tobytes()

@app.get("/")
async def root():
    return {"message": "It's working!"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    nobg_image = await remove_background(file)
    return Response(content=nobg_image, media_type="image/png")