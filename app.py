from flask import Flask, render_template, request
from noa import passing_data
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('result.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

      return render_template("result.html",result = passing_data(result))
   else:
      return render_template("result.html",result="")
if __name__ == '__main__':
   app.run(debug = True)
