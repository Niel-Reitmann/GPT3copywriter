from flask import Flask, request, render_template
from copywriter import generate_text

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/improve', methods=['POST'])
def improve():
  prompt = request.form['text']
  improved_text = generate_text(prompt)
  return render_template('home.html', improved_text=improved_text)

if __name__ == '__main__':
  app.run()
