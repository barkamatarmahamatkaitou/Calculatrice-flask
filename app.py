from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculatrice():
    resultat = ""
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        if op == "+": resultat = a + b
        elif op == "-": resultat = a - b
        elif op == "*": resultat = a * b
        elif op == "/": 
            if b == 0:
               resultat = "Erreur: Division par 0" 
            else:
                resultat = a / b
        elif op == "**": resultat = a ** b
    return render_template("index.html", resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
