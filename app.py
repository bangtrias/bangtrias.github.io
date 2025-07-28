from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        bb = float(request.form["bb"])
        tb = float(request.form["tb"])
        sl = float(request.form["sl"])
        cm = float(request.form["cm"])
        st = float(request.form["st"])
        di = float(request.form["di"])

        bsa = ((tb * bb) / 3600)* 0.5
        bsa_mod = ((sl * bb) / 3600)* 0.5
        volume_cm = (12.753 * bsa)/ (cm/1000)
        volume_cm_mod = (12.753 * bsa_mod)/ (cm/1000)
        delay = di + (5-(st / 2))

        results = {
            "bsa": round(bsa, 6),
            "bsa_mod": round(bsa_mod, 6),
            "volume_cm": round(volume_cm, 6),
            "volume_cm_mod": round(volume_cm_mod, 6),
            "delay": round(delay, 2)
        }

        return render_template("index.html", results=results)
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
