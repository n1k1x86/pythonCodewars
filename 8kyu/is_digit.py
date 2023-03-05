def isDigit(string):
    print(string)
    try:
        return True if str(float(string)) or str(int(string)) else False
    except:
        return False