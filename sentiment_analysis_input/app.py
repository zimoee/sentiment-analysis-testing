from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_text(text):
    blob = TextBlob(text)
    subjectivity = blob.sentiment.subjectivity
    polarity = blob.sentiment.polarity
    return subjectivity, polarity

@app.route('/', methods=['GET', 'POST'])
def index():
    subjectivity = None
    polarity = None
    if request.method == 'POST':
        text = request.form['text']
        subjectivity, polarity = analyze_text(text)
    return render_template('index.html', subjectivity=subjectivity, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
