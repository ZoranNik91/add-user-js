from flask import Flask, jsonify, request, render_template
from arrival import get_by_date 

app = Flask(__name__, static_url_path='')

# WEB

@app.route('/')
def root():
    #Renders a template from the template folder with the given context
    return render_template("index.html", title = 'DOLASCI ZA DAN')


# API

@app.route('/api/date')
def by_date():

    date = request.args.get('date')
    res = get_by_date(date)

    return jsonify(res)




if __name__ == '__main__':
    app.run()