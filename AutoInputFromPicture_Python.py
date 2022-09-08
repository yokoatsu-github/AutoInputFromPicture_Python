import os
from PIL import Image
import pyocr

#環境変数「PATH」にTesseract-OCRのパスを設定。
path='/bin/tesseract.exe'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'/bin/tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#文字を抽出したい画像のパスを選ぶ
img = Image.open('/home/71728648/picture/number2.jpg')

#画像の文字を抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="eng", builder=builder)

print(text[12])