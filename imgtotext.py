import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/Users/umamaheswarikannan/PycharmProjects/untitled/venv/lib/python2.7/site-packages/pytesseract/pytesseract.py'
print(pytesseract.image_to_string(r'text.png'))