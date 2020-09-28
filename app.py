from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from rephraseService import generateQuestions

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/questions", methods = ['POST'])
def questions():
  requestData = request.get_json()
  questions = generateQuestions(requestData['q'])
  return jsonify(questions)
  
app.run()