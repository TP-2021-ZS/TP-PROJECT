def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        Lines = file.readlines()

        return Lines
    except:
        return False
