# Flask upload file

Simple API to demonstart how to handle file upload in flask with REST API.

## Python version
3.8.10

## Installation
Install the requirements. 
In your terminal, run:
```bash
pip install -r requirements.txt
```

## Run the API
In your terminal, run:
```bash
python app.py
```

## Routes
`GET '/'`
Return `Alive` if the server is running.

`POST '/predict'`
With a body of type `form-data`:
```json
{
    "image": image_here,
}
```
Return:
```json
{
    "prediction": your_prediction_here,
}