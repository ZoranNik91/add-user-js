from flask import Flask, jsonify, request
from arrival import get_by_date 

app = Flask(__name__)


@app.route('/api/date')
def by_date():

    date = request.args.get('date')
    res = get_by_date(date)

    return jsonify(res)

if __name__ == '__main__':
    app.run()