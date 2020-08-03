from fastapi import FastAPI, File, UploadFile

import easyocr

app = FastAPI()

reader = easyocr.Reader(['en'])


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    fileName = file.filename
    predictions = recognize(file.file)

    response = {}

    for idx, prediction in enumerate(predictions):
        text = []
        coords = []
        for array, word, confidence in prediction:
            print(word, confidence)
            # text.append(word)
            # coords.append(array.tolist())

    # response[fileName] = {"text": word, "coords": coords}
    print(predictions)
    return True


def recognize(img):
    predictions = result = reader.readtext(img)
    return predictions
