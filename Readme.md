Build

```
docker build -t akshay090/ocr:keras-ocr .
```

Run 

```
docker run --gpus all -v ~/akshay/OCR.Docker:/app -p 80:80 akshay090/ocr:keras-ocr
```

Test API

```
curl --location --request POST 'http://127.0.0.1:80/kerasocr/' --form 'file=@/home/sign.jpg'
```