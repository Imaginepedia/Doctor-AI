import random
import flask
import numpy
import assist
import pandas as pd
import math
import time


def blood_pressure():
    s=numpy.array(range(115,130))
    d=numpy.array(range(75,90))
    systole=random.choice(s)
    diastole=random.choice(d)
    assist.speak(f"Your Blood Pressure is :{systole}/{diastole}")

def pulse():
    p=numpy.array(range(65,100))
    puls=random.choice(p)
    assist.speak(f"your pulse is : {puls}")

def temperature():
    temp=random.uniform(97,99)
    assist.speak(f"Your present temperature is: {temp:.1f}°F")
