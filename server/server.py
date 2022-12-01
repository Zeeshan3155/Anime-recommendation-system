from flask import Flask, jsonify, request
import util

app = Flask(__name__)



@app.route("/recommend", methods = ['GET', 'POST'])
def recommend():
    title = request.form['title']
    no_recommend = int(request.form['top_n'])
    response =  jsonify(util.get_recommendation(title,no_recommend))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting flask server")
    util.load_artifacts()
    app.run()