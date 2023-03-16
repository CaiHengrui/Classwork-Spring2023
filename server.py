from flask import Flask, request, jsonify
#flask has a module/function called request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server On"


@app.route("/info", methods={"GET"})
def info_route():
    return "This server was written for BME 547"
#http://127.0.0.1:5000/info



#$ python server.py
#  * Serving Flask app 'server'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use
# a production WSGI server instead.
#  * Running on http://127.0.0.1:5000

@app.route("/HDL_analysis", methods=["POST"])
def HDL_route_handler():
    """
    in_data = {"name": <patient_name>,
               "HDL_value": <HDL_result> }
    """
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    print("Received HDL value of {}".format(in_data["HDL_value"]))
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis


@app.route("/add", methods=["POST"])
def add_numbers():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    if answer < 0:
        return "The answer was less than zero. BAD", 400
    return jsonify(answer) #can not return a int so it need to be converted into json(string)
# need to unjsonify in client.py
#int() or r.json() [not use .text]


@app.route("/add_two/<a>/<b>", methods=["GET"])
def add_two_handlere(a, b): # a b are strings
    answer = int(a) + int(b)
    return jsonify(answer)



if __name__ == '__main__':
    app.run()