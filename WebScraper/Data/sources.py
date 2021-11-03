def read_url_file(filename):
    try:
        file = open(filename, 'r')
        Lines = file.readlines()

        return Lines
    except:
        return False
