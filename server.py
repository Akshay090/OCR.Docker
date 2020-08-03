from fastapi import FastAPI, File, UploadFile
import json
import numpy
import easyocr

app = FastAPI()

reader = easyocr.Reader(['en'])


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    fileName = file.filename
    contents = file.file.read()
    predictions = recognize(contents)

    response = {}
    text = []
    coords = []
    for idx, prediction in enumerate(predictions):
        cords, word, confidence = prediction
        print(word)
        text.append(word)
        coords.append(cords)
        
    response[fileName] = {"text": text, "coords": coords}
    print(response)
    return json.dumps(response, default=convert)


def recognize(img):
    predictions = reader.readtext(img)
    return predictions

def convert(o):
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError