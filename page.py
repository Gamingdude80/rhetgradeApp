from flask import Flask,render_template,request,flash
import os
from rhetgrade import Grader

ALLOWED_EXTENSIONS = {"txt"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.getcwd()+"/uploads/"
app.config["SECRET_KEY"] = os.urandom(12)

@app.route("/", methods=["GET", "POST"])
def mainPage():
    labels = ["lead","position","claim","counterclaim",
            "rebuttal","evidence","counter claim"]
    if request.method == "POST":
        temp = getFile()
        if temp:
            return render_template('main.html', title = "Main page")
        modelName = request.form["ModelName"]
        try:
            grader = Grader(app.config['UPLOAD_FOLDER']+"document.txt",
                        modelName)
        except:
            flash("Model not found")
            return render_template('main.html', title = "Main page")
        results = [grader.reader.paragraphs,
                    grader.categorize(labels,most_accurate=True)]
        grader.reader.blank_file()
        return render_template("results.html", title = "Results",
                results = results, length = len)
    return render_template('main.html', title = "Main page")

@app.route("/about")
def aboutPage():
    return render_template("about.html", title = "About")

def getFile():
    if 'file' not in request.files:
        flash("File was not found")
        return True
    file = request.files["file"]
    if file.filename == "":
        flash("No File Selected")
        return True
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],"document.txt"))
        file.close
        return False
    flash("File type not available for processing")
    return False

def resultDisplay(catagorized):
    displayStrings = []
    for x,paragraph in enumerate(catagorized[0]):
        displayString = ""
        for y,sentence in enumerate(paragraph):
            displayString+=("{" + sentence + catagorized[1][x][y] + "} ")
        displayStrings.append(displayString)
    return displayStrings

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True)