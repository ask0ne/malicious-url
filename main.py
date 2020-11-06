'''
URL APP
'''
import pickle
import flask
from flask import Flask

FLASK_APP = Flask(__name__, template_folder='templates')

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'www' in total_Tokens:
        total_Tokens.remove('www')	#removing .com since it occurs a lot of times and it should not be included in our features
    if 'com' in total_Tokens:
        total_Tokens.remove('com')
    if 'http' in total_Tokens:
        total_Tokens.remove('http')
    return total_Tokens


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
        prediction = predict(query)
        return flask.render_template('index.html', result=prediction)


@FLASK_APP.route('/predict', methods=['POST'])
def predict(query):
    '''
    Load pretrained scikit-learn model, evaluate input URL and output prediction
    '''
     # load the vectorizer
    loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
    # load the model
    loaded_model = pickle.load(open('classification.model', 'rb'))
    result = loaded_model.predict(loaded_vectorizer.transform([query]))
    print(result)
    if result[0] == 'benign':
        result = 'SAFE :)'
    else:
        result = 'NOT SAFE :('
    return result

if __name__ == '__main__':
    FLASK_APP.run()
