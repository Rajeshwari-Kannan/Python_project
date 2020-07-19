import pytesseract
def imgConvert(p_file):
   v_imgtotext=pytesseract.image_to_string(p_file)
   return v_imgtotext