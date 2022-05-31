# Flask upload file

Simple API to demonstart how to handle file upload in flask with REST API.

## Routes
`GET '/'`
Return `Alive` if the server is running.

`POST '/Predict'`
With a body of type `form-data`:
```json
{
    "image": image_here
}
```
Return:
```json
{
    "prediction": your_prediction_here,
    "image_path": your_file_path_on_the_server_here
}