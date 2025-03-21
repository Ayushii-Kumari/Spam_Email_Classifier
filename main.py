import email
from flask import Flask,render_template,request
import pickle 

cv = pickle.load(open("cv.pkl","rb"))
clf = pickle.load(open("clf.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def EmailSpamClassifier():
    return render_template("EmailSpamClassifier.html")


@app.route("/predict",methods=["POST"])
def predict():
    email = request.form.get("content")
    tokenized_email = cv.transform([email])
    prediction = clf.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    
    return render_template("EmailSpamClassifier.html",prediction=prediction,email=email)

if __name__ == "__main__":
    app.run(debug=True)
