from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_file,
    Response,
)
from werkzeug.utils import secure_filename

from s3_bucket import (
    file_upload,
    file_download,
    list_of_files,
)

app = Flask(__name__)
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
BUCKET_NAME = "data-awesome-bucket"


def allowed_file(filename: str) -> bool:
    """
    The function checks whether the file extension is in `ALLOWED_EXTENSIONS`.
    """
    return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home_page() -> str:
    """
    The function returns information about the application.
    """
    return "A simple Flask app to upload binary data to Amazon S3 storage."


@app.route("/bucket")
def bucket() -> str:
    """
    The function returns .html page with contents.
    """
    contents = list_of_files(BUCKET_NAME)

    return render_template("index.html", contents=contents)


@app.route("/upload", methods=["POST"])
def upload() -> Response:
    """
    The function checks whether the user has selected a file
    and whether the file extension is valid.
    """
    if request.method == "POST":
        if "file" not in request.files:
            return redirect("/bucket")

        file = request.files["file"]

        if not file.filename:
            return redirect("/bucket")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            file_upload(f"{filename}", BUCKET_NAME)
            return redirect("/bucket")


@app.route("/download/<filename>", methods=["GET"])
def download(filename: str) -> Response:
    """
    The function allows the user to upload an existing file.
    """
    if request.method == "GET":
        filename = secure_filename(filename)
        output = file_download(filename, BUCKET_NAME)

        return send_file(output, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
