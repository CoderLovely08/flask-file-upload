from flask import Flask, render_template, request
from flask import *  
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test',methods=['GET','POST'])
def test():
    if request.method== ('POST' or 'GET'):
        myfile = request.files['fileInput']
        if '.xlsx' in myfile.filename:
            print("Excel file working")
            myfile.save(myfile.filename)
            myfun(myfile)
        else: return render_template("Failure.html") 
    return render_template("success.html", name = myfile.filename) 

def myfun(file):
    data=pd.read_excel(f"{file.filename}")
    rows=int(data.shape[0])
    print(rows)

if __name__ == "__main__":
    app.run(debug=True)