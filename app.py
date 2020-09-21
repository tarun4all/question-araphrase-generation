from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from rephraseService import generateQuestions

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/questions")
def questions():
  question = request.args.get('q')
  questions = generateQuestions(question)
  return jsonify(questions)
  
app.run()