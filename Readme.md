Build

```
docker build -t easy-ocr-api .
```

Run 

```
docker run --gpus all -d --name easy-ocr -p 80:80 easy-ocr-api
```

Test API

```
curl --location --request POST 'http://127.0.0.1:80/uploadfile/' --form 'file=@/home/sign.jpg'
```