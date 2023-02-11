import pyocr
from PIL import Image, ImageEnhance
import os
from flask import Flask, request
import json

app = Flask(__name__)
tool = pyocr.get_available_tools()[0]

@app.route("/", methods=["POST"])
def ocr():
    try:
        filename = request.files['file'].filename if 'file' in request.files else ''
        if filename == '':
            return '{"success":false,"message":"No file chosen."}'
        img = Image.open(filename)
        img = img.convert('L')
        img = ImageEnhance.Contrast(img).enhance(2.0)
        text = tool.image_to_string(img, lang='jpn', builder=pyocr.builders.TextBuilder(tesseract_layout=6))
        return json.dumps({'success': True, 'data': text})
    except Exception as e:
        print(e)
        return '{"success":false,"message":"Failed to OCR uploaded file."}'
