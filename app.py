from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

@app.route("/")
def route_1():
    return "<h1>Welcome to My Flask API!</h1>"


@app.route("/about")
def route_2():
    return jsonify({"name": "Miriam Stern", "course": "MCON-504 - Backend Development", "semester": "Spring 2026"})

@app.route("/greet/<name>")
def route_3(name):
    print(request)
    return f"<p>Hello {name}, ! Welcome to Flask.</p>"


@app.route("/calculate")
def route_4():
    print(request)
    operation= request.args["operation"]
    operand1=request.args["num1"]
    operand2=request.args["num2"]
    result = None
    if operation == 'add':
        result = int(operand1) + int(operand2)

    elif operation == 'sub':
        result = int(operand1) - int(operand2)
    return f"<p>result = {result}<p>"



@app.route("/echo", methods=['POST'])
def route_5():
    posted = request.get_json()
    posted["echoed"] = True
    return jsonify(posted)

@app.route("/status/<int:code>")
def route_6(code):
    message = f"This is a {code} error"
    return message



if __name__ == '__main__':
    app.run(debug=True, port=5000)