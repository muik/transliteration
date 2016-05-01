import os
import tensorflow as tf
import numpy as np
import data_utils
import subprocess
from translate import Transliteration
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
transliteration = Transliteration()

def is_learned(input):
  return 0 == subprocess.call(['grep', '-i', '^%s$' % input, 'data/giga-fren.release2.en'])

@app.route("/", methods=['GET'])
def main():
  return render_template('index.html')

@app.route("/", methods=['POST'])
def transliterate():
  input = request.form['input']
  output = transliteration.run(input)
  learned = is_learned(input)
  return jsonify({'input': input, 'output': output, 'learned': learned})

if __name__ == "__main__":
#  app.debug = True
  app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

