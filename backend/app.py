from flask import Flask, request, jsonify, send_file, redirect, url_for, flash, make_response
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
from user import user
from dotenv import load_dotenv
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


app.register_blueprint(user, url_prefix="/user")

# Ensure storage folder exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello World!"})

@app.route("/logout", methods=["POST", "GET"])
def logout():
    response = make_response(redirect(url_for("home")))
    ## Clear the cookie from serverSide
    response.set_cookie('jwt', '', expires=0, path="/")

    flash("Log out successful", "success")
    return response

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)
    return jsonify({"message": "File uploaded successfully", "file": filename})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True)
