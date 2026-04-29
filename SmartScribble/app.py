from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Eduportal():
    return render_template("eduportal.html")

print("WSGI server gracefully initiated with the port number 8000.")

if __name__ == "__main__":
    app.run(port=8000)