from flask import Flask
helloworld = Flask(_name_)
@helloworld.route("/")
def run():
    return "{\"message\": \"Hello World Program v1\"}"
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)