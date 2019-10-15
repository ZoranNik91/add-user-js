from flask import Flask, jsonify, request, render_template
from arrival import get_by_date 

app = Flask(__name__, static_url_path='')

# WEB

@app.route('/') # #1
def root():
    #Renders a template from the template folder with the given context
    return render_template("index.html", title = 'DOLASCI ZA DAN')


# API

@app.route('/api/date')
def by_date():

    date = request.args.get('date') # #2
    res = get_by_date(date)

    return jsonify(res)




if __name__ == '__main__':
    app.run()







'''
#1
In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned
from other functions as well. Functions can be defined inside another function and 
can also be passed as argument to another function.
Decorators are very powerful and useful tool in Python since it allows programmers to modify
the behavior of function or class. Decorators allow us to wrap another function in order to
extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called
inside the wrapper function.

Syntax for Decorator:

    @gfg_decorator
    def hello_decorator(): 
        print("Gfg") 
  
    Above code is equivalent to - 
  
    def hello_decorator(): 
        print("Gfg") 
      
    hello_decorator = gfg_decorator(hello_decorator)


#2  
.get() is a method of the dict class. So as any dictionaries behavior, if you do:

my_dict = {'Name': 'Daniel',  'Age': 22}
name = my_dict.get('Name')
age = my_dict.get('Age')

name will be the same datatype as the data in the dictionary.
For example, name will be a string type and age will be a integer type. 

flask.Request.args
A MultiDict with the parsed contents of the query string. (The part in the URL after the question mark).

So the args.get() is method get() for MultiDict, whose prototype is as follows:

get(key, default=None, type=None)

'''