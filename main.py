from flask import Flask
import random
from flask import render_template
from flask import request

app = Flask(__name__)



@app.route('/')

def render_home():
    return render_template('home.html')

@app.route('/ctof')

def render_ctof():

    return render_template('ctof.html')

@app.route('/ctof_result')

def render_ctof_result():
    try:
        ctemp_result = float(request.args['ctemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', 
                               ctemp=ctemp_result, 
                               ftemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ftoc')

def render_ftoc():

    return render_template('ftoc.html')

@app.route('/ftoc_result')

def render_ftoc_result():
    try:
        ftemp_result = float(request.args['ftemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html',
                              ftemp=ftemp_result, 
                              ctemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/mtokm')

def render_miles():

    return render_template('mtokm.html')

@app.route('/mtokm_result')

def render_mtokm_result():
    try:
        miles_result = float(request.args['miles_str'])
        km_result = convert_miles(miles_result)
        return render_template('mtokm_result.html',
                              miles_str=miles_result, 
                              km=km_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/random')


def render_random():

    return render_template('random.html')

@app.route('/random_result')

def render_random_result():
    try:
        limit = float(request.args['rand_num'])
        list1 = randNums(limit)
        return render_template('random_result.html', 
                           result = list1)
    except ValueError:
        return "Sorry: something went wrong"
    

def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)



@app.route('/ftoc/<ftemp_str>')

def convert_ftoc(ftemp_str):

    ftemp = 0.0

    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Fahrenheit: " + ftemp_str + " In Celsius: " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"

def ctof(ctemp):
    return (ctemp*(9/5)) + 32
@app.route('/ctof/<ctemp_str>')

def convert_ctof(ctemp_str):
    try:
        ctemp = float(ctemp_str)

        ftemp = ctof(ctemp)
        return "In Celsisu: " + ctemp_str + " In Fahrenheit: " + str(ftemp)
    except ValueError:
        return "Sorry.  Could not convert " + ctemp_str + " to a number"
    

def miles_to_km(miles): 
    return (miles * 1.609344)


@app.route('/mtokm/<miles_str>') 

def convert_miles(miles_str):
    try:
        miles = float(miles_str)
        km = miles_to_km(miles)
        return km
    except ValueError:
        return "Sorry.  Could not convert " + miles_str + " to a number"

def rand(randNum):
    num1 = []
    for i in range(10):
        num1.append(str(random.randint(1,randNum)))
    return num1



@app.route('/random/<rand_num>')


def randNums(rand_num):
    randN = int(rand_num)
    try:
        rand1 = rand(randN)
        return  ", ".join(rand1)
    except ValueError:
        return "Sorry.  Could not convert " + rand_num + " to a number"


if __name__ == "__main__":
   app.run(host='0.0.0.0')