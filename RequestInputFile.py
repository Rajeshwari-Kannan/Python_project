def req_Input(p_file):
    v_file=input("Enter the file name:")
    if v_file is None or v_file=='':
        return p_file
    else:
        return v_file