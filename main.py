from flask import Flask
import random

app = Flask(__name__)

@app.route("/")

def hello():
   return "Hello World!"

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
        return "In miles: " + miles_str + " In Kilometers: " + str(km)
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