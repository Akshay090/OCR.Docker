from fastapi import FastAPI, File, UploadFile

import keras_ocr

import tesserocr

from PIL import Image


app = FastAPI()

pipeline = keras_ocr.pipeline.Pipeline(scale=3)


@app.post("/kerasocr/")
def create_upload_file(file: UploadFile = File(...)):
    fileName = file.filename
    predictions = recognize(file.file)

    response = {}

    for idx, prediction in enumerate(predictions):
        text = []
        coords = []
        for word, array in prediction:
            text.append(word)
            coords.append(array.tolist())

    response[fileName] = {"text": word, "coords" :coords}
    print(predictions)
    return response


def recognize(img):
    # actually here's only 1 image in this list
    images = [keras_ocr.tools.read(img)]
    predictions = pipeline.recognize(images)
    return predictions


@app.post("/tesserocr/")
async def upload_file(file: UploadFile = File(...)):
    print('hello')
    image = Image.open(file.file)
    res = tesserocr.image_to_text(image)
    return res
