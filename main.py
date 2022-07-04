from flask import Flask, jsonify, render_template

app = Flask(__name__)
@app.route("/")
def inicio():
  return render_template("index.html")

@app.route("/<num>")
def contaPares(num):
    pares = []
    impares = []
    for i in range(int(num)+1):
        if i % 2 == 0:
            pares.append(i)
            continue
        else:
            impares.append(i)
            continue
    return jsonify({"pares":pares}, {"impares":impares})

app.run(host="0.0.0.0")