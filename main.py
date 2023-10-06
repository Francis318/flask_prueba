from flask import Flask, request, make_response, redirect

app= Flask(__name__)

@app.route("/")
def index():
    ip=request.cookies.get("user_ip")
    return f"<h1>Hello, Koder Your IP is:{ip} </h1>"

@app.route("/ip")
def get_id():
    ip=request.remote_addr
    response=make_response(redirect("/"))
    response.set_cookie("user_ip", ip)
    response.set_cookie("mas_info", "Esta es una cookie")
    return response


@app.route("/method", methods=["POST","GET"])
def get_method():
    method=request.method
    return f"El metodo de la solicitud es: {method}"

@app.route("/headers")
def get_headers():
    headers=request.headers
    return dict(headers)