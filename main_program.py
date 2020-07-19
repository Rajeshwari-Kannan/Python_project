import RequestInputFile
import imgtotext
import PrintOutputString

v_file=RequestInputFile.req_Input()
v_text=imgtotext.imgConvert(v_file)
PrintOutputString.getResult(v_text)

