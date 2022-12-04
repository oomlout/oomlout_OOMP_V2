from flask import Flask,redirect, url_for, render_template
import OOMP
import OOMP_summaries_BASE
import markdown


app = Flask(__name__, template_folder="oomlout_OOMP_flask_V2/templates")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/part/<name>")
def user(name):
    try:
        item = OOMP.items[name]
    except KeyError:
        try:
            item = OOMP.itemsHex[name]
        except KeyError:
            return "Part not found."
    pageContent = OOMP_summaries_BASE.generateReadme(item, mode = "flask")
    md = markdown.markdown(pageContent, extensions=['tables'])
    return md
    

@app.route("/list/<name>")
def list(name):
    return render_template("index.html",content=name, list2 = [0,1,2,3])


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    OOMP.loadPickle()
    app.run()

