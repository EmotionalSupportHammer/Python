from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    username = request.cookies.get("username")
    views = int(request.cookies.get("views", 0)) + 1

    print("Cookies received by server:", dict(request.cookies))

    if username:
        resp = make_response(f"Welcome back, {username}. Total views: {views}")
    else:
        resp = make_response(f"First visit — setting cookie. Total views: {views}")
        resp.set_cookie("username", "student123", max_age=60, path="/")

    resp.set_cookie("views", str(views), max_age=300, path="/")  # lasts 5 min
    return resp

@app.route("/delete")
def delete_cookie():
    resp = make_response("Cookie deleted")
    resp.set_cookie("username", "", max_age=0, path="/")
    return resp

# Run locally
app.run(debug=True)