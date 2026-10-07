from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/students" , methods=[GET])
def students():
    return jsonify({
    "name":"suyog",
    "roll":67
    })
if __name__=="__main__":
    app.run(debug=True);