from flask import Flask, jsonify, request

app = Flask (__name__)
glucose=[
    
    {
        "glucose_id" : "1",
        "date" : ["September 1, 2022"],
        "glucose" : ["115"]
    },
    {
        "glucose_id" : "2",
        "date" : ["September 2, 2022"],
        "glucose" : ["117"]
    },
   
]

@app.route('/glucose', methods=['GET'])
def displayGLucose():
    return jsonify(glucose)

if __name__ == '__main__':
    app.run()