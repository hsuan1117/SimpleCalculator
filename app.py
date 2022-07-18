from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/calc')
def calc():
    try:
        result = eval(request.json["formula"])
    except Exception:
        result = "Error"

    return jsonify({
        "result": result
    })


if __name__ == '__main__':
    app.run()
