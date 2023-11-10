from myfunctions import mysqrt, mysin, mycos, myarcsin, sin45, cos45
from myhaversine import myhaversine
import math
import csv

def main():
    test_mysqrt()
    test_mysin()
    test_mycos()
    test_myarcsin()
    test_myhaversine()

def test_mysqrt():
    x=2 #x apenas igual ou superior a 0 pois, se x menor que 0, o return é logo 0
    assert round(mysqrt(x), 2) == round(x**0.5, 2)

def test_mysin():
    assert mysin(30) == sin45(30)
    assert mysin(50) == cos45(90-50)
    assert mysin(100) == mysin(180-100)
    assert mysin(200) == -mysin(200-180)

def test_mycos():
    assert mycos(30) == cos45(30)
    assert mycos(50) == sin45(90-50)
    assert mycos(100) == -mycos(180-100)
    assert mycos(200) == -mycos(200-180)

def test_myarcsin():
    x=0.5 #x está logo definido para estar compreendido entre -1 e 1
    assert round(myarcsin(x), 2) == round(math.degrees(math.asin(x)), 2)

def test_myhaversine():
    p1=90,-100
    p2=50,-180
    assert myhaversine(p1,p2)-0.1 < myhaversine(p1,p2) < myhaversine(p1,p2)+0.1


if __name__ == "__main__":
    main() 
