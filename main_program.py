import RequestInputFile
import imgtotext
import PrintOutputString

class MainClass:
    filepath=r'/Users/umamaheswarikannan/PycharmProjects/Python_project/text1.png'

m1=MainClass()
v_file=RequestInputFile.req_Input(m1.filepath)
v_text=imgtotext.imgConvert(v_file)
PrintOutputString.getResult(v_text)

