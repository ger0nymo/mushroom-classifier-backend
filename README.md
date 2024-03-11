Flask backend server setting up a POST endpoint that can receive an image, run the loaded model, and return a prediction to the client.

## Example request
```http request
POST .../upload 
```

Payload Type: Multipart Form-Data

```typescript
interface Payload {
    file: File,
}
```

Expected Successful Result: Http Status Code - 200

```json
{
    "predictions": [
        {
            "name": "Agaricus bisporus",
            "prob": 0.7407903075218201
        },
        {
            "name": "Pleurotus cystidiosus",
            "prob": 0.24722404778003693
        },
        {
            "name": "Coprinus comatus",
            "prob": 0.003535553580150008
        },
        {
            "name": "Lentinus edodes",
            "prob": 0.00287005421705544
        },
        {
            "name": "Agaricus blazei Murill",
            "prob": 0.002500273287296295
        }
    ]
}

```
