import email
from flask import Flask,render_template,request
import pickle 

cv = pickle.load(open("cv.pkl","rb"))
clf = pickle.load(open("clf.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def EmailSpamClassifier():
    return render_template("EmailSpamClassifier.html")


@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('content')
    prediction = model_predict(email)
    return render_template("index.html", prediction=prediction, email=email)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = model_predict(email)
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
