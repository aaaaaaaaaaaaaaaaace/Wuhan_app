from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def default():
    return render_template("index.html")

@app.route('/temperatured')
def temperatured():
    temperature = request.args.get('temperature')
    temperature = float(temperature)
    if temperature:
        if 38.0 <= temperature < 45.0:
            return render_template('infected.html', temperature = temperature)
        elif 30.0 < temperature < 38.0:
            return render_template('normal.html', temperature = temperature)
        else:
            return render_template('weird.html', temperature = temperature)
    else:
        return render_template('index.html', temperature = temperature)

if __name__ == '__main__':
    app.run(debug=True) 


