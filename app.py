import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from prediction import Prediction

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

model = YOLO('best.pt')
print('Model loaded')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        prediction = model(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        names = prediction[0].names
        top5_idx = prediction[0].probs.top5
        top5_probs = prediction[0].probs.top5conf

        top5 = []
        for i in range(5):
            top5.append({"name": names[top5_idx[i]], "prob": top5_probs[i].item()})

        result = Prediction(top5).json()

        # If probability of the first prediction is greater than 0.7, move the image to a folder with the corresponding class name.
        # This could later be used to retrain the model with the new images.
        if top5_probs[0].item() > 0.7:
            os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], names[top5_idx[0]]), exist_ok=True)
            os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename),
                      os.path.join(app.config['UPLOAD_FOLDER'], names[top5_idx[0]], filename))
        else:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print(result)

        return result
    else:
        return 'File type not allowed'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)