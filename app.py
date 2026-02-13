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
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    operation = request.args.get('operation')
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result, "operation": operation})
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500



@app.route("/echo", methods=['POST'])
def route_5():
    posted = request.get_json()
    posted["echoed"] = True
    return jsonify(posted)

@app.route("/status/<int:code>")
def route_6(code):
    message = f"This is a {code} error"
    return message, code

@app.before_request
def before_request():
    method = request.method
    path = request.path
    print(f"Method: {method} Path: {path}")

@app.after_request
def after_request(response):
    response.headers["X-custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def teardown_request(error):
    if error:
        print(f"There was a exception: {error}")

@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)



if __name__ == '__main__':
    app.run(debug=True, port=5000)