1. What does the @app.route() decorator actually do?
2. How does Flask know which function to call when a request arrives?
3. What's the difference between route parameters (<name>) and query parameters (?key=value)?
4. Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
5. What happens if you try to access request.args outside of a request context?


1. It shows you all your registered routes.
2. depending on the request URL
3. route parameters become part of the URL so they are required.
    query parameters are used if you want to filter the results
4. When we post something, we are creating a new JSON file so you have access it using request.get_json
    when we get something the data is in the URL so you use request.args.get() to access it
5. RuntimeError because the request only exists while flask is working on a request 