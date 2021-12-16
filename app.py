from flask import Flask, render_template, request
import datetime
import model_py
from dateutil import parser

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      names = request.form['fname']
      gender = request.form['gender']
      romantic = request.form['romantic']
      birthday = request.form['birthday']
      # first_time = datetime.strptime(birthday, "%Y/%m/%d")
      dt = parser.parse(birthday)
      # first_time = pd.to_datetime(birthday)
      later_time = datetime.datetime.today()
      age = later_time.year - dt.year
      
      nursery = request.form['nursery']
      higher_ed = request.form['higher_ed']
      school = request.form['school']
      paid = request.form['paid']
      famsup = request.form['famsup']
      schoolsup = request.form['schoolsup']
      activities = request.form['activities']
      cat_1 = request.form['cat_1']
      cat_2 = request.form['cat_2']
      failures = request.form['failures']
      absences = request.form['absences']
      Studytime = request.form['Studytime']
      
      guardian = request.form['guardian']
      Parents_status = request.form['Parents_status']
      famsize = request.form['famsize']
      mjob = request.form['mjob']
      medu = request.form['medu']
      fedu = request.form['fedu']
      fjob = request.form['fjob']
      
      traveltime = request.form['traveltime']
      freetime = request.form['freetime']
      goout = request.form['goout']
      internet = request.form['internet']
      health = request.form['health']
      
      X_test = [[school,gender,age,famsize,Parents_status,medu,fedu,mjob,fjob,guardian,traveltime,Studytime,failures,schoolsup,famsup,paid,activities,nursery,higher_ed, internet, romantic, freetime,goout,health,absences,cat_1,cat_2]]

      prediction = str(model_py.regressionAnalysis(X_test))
      return render_template("index.html", prediction = prediction[1:3], names = names, grade = model_py.grade(model_py.regressionAnalysis(X_test)))

if __name__ == '__main__':
    app.run(debug = True)