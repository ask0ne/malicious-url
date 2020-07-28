'''
URL APP
'''
import flask
#import pickle
from flask import Flask
FLASK_APP = Flask(__name__, template_folder='templates')


@FLASK_APP.route("/", methods=['GET', 'POST'])
def main():
    '''
    INDEX PAGE
    GET method when page loads
    POST method when query
    '''
    if flask.request.method == 'GET':
        return flask.render_template('index.html', result=None)
    if flask.request.method == 'POST':
        query = flask.request.form['query']
        prediction = query
        return flask.render_template('index.html', result=prediction)


@FLASK_APP.route('/predict', methods=['POST'])
def predict():
    '''
     json = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = lr.predict(query)
     return jsonify({'prediction': list(prediction)}) '''

if __name__ == '__main__':
    FLASK_APP.run()
