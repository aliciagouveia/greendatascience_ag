from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format(): #to test if the format is correct
    assert validate (r'1.2.3.4') == True
    assert validate (r'1.2.3') == False
    assert validate (r'1.2') == False
    assert validate (r'1') == False

def test_range (): #to test if the range 0-255 is correct
    assert validate (r'255.255.255.255') == True
    assert validate (r'2000.255.255.255') == False
    assert validate (r'255.2000.255.255') == False
    assert validate (r'255.255.2000.255') == False
    assert validate (r'255.255.255.2000') == False

if __name__ == "__main__":
    main()