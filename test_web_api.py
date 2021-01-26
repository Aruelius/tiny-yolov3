import os

from flask import Flask, jsonify, request
from PIL import Image

from yolo import YOLO


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
yolox = YOLO()


@app.route("/test", methods=["POST"])
def test():
    jpgfile = request.files.get("file")
    if not jpgfile:
        return jsonify(code=403, msg="empty file")
    img = Image.open(jpgfile)
    result = yolox.detect_image(img, distance=True)
    return jsonify(code=0, data=result, msg="success")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
