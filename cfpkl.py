

from flask  import Flask,request
import pandas as pd
import numpy as np
import pickle

app= Flask(__name__)
pickel_in=open("cf.pkl","rb")
cf= pickle.load(pickel_in)
@app.route('/')
def Welcome():
  return "welcome all"

@app.route('/predict')
def predict_note_authentication():
    variance =request.args.get('variance')
    skewness =request.args.get('skewness')
    curtosis =request.args.get('curtosis')
    entropy =request.args.get('entropy')
    prediction= cf.predict([[variance,skewness,curtosis,entropy]])
    return str(prediction)




if __name__ == '__main__':
  app.debug = True
  app.run()