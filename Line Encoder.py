# DC Assignment - Implementing Line Encoding Schemes using Line Encoder and Scrambler 

# Python Libraries being used are - Turtle, Tkinter, Random and String
# Author - Zeeshan Chowdhary 
# Dated - 26th of November, 2022

import turtle
import tkinter as tk
import random
import string

# NRZ-I : Non Return to Zero (Inverted)
class NRZ_I:
    
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        t.sety(self.logic_high)
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.forward(self.distance)

    def one(self):
        posx, posy = t.pos()
        if self.logic_low - 1 < posy < self.logic_low + 1:
            t.sety(self.logic_high)
        elif self.logic_high - 1 < posy < self.logic_high + 1:
            t.sety(self.logic_low)
        t.forward(self.distance)
        print(posy)

# NRZ-L : Non Return to Zero (Level)
class NRZ_L:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)

# Manchester
class Manchester:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)
        setTurtle(*invisiline)
        t.write('0', False, 'center', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.sety(self.logic_low)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)
        t.sety(self.logic_high)
        setTurtle(*invisiline)
        t.write('1', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)

# AMI : Alternate Mark Inversion
class AMI:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        temp=0
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                temp+=1
                count=temp%2
                if count==1:
                    self.onepos()
                elif count == 0:
                    self.oneneg()

    def zero(self):
        t.sety(self.base)
        t.forward(self.distance)

    def onepos(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def oneneg(self):
        t.sety(self.logic_low)
        t.forward(self.distance)

# B8ZS : Bipolar Eight Zero Substitution
class B8ZS:
    def __init__(self, signal: str):
        self.signal = signal
        x=0
        counter=0
        for i in self.signal:
            counter+=1
            if i == '0':
                x+=1
                if x==8:
                    self.signal=self.signal[:counter-8]+'000VB0VB'+self.signal[counter:]
                    x=0
            elif i == '1':
                x=0
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        temp=0
        for i in self.signal:
            if i == '0':
                self.zero()
            else:
                if i=='1' or i=='B':
                    temp+=1
                elif  i == 'V':
                    temp=temp
                count=temp%2
                if count==1:
                    self.onepos()
                elif count == 0:
                    self.oneneg()

    def zero(self):
        t.sety(self.base)
        t.forward(self.distance)

    def onepos(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def oneneg(self):
        t.sety(self.logic_low)
        t.forward(self.distance)

# HDB3 : High Density Bipolar 3
class HDB3:
    def __init__(self, signal: str):
        self.signal = signal
        x=0
        y=0
        counter=0
        for i in self.signal:
            counter+=1
            if i == '0':
                x+=1
                if x==4:
                    if y%2==0:
                        self.signal=self.signal[:counter-4]+'B00V'+self.signal[counter:]
                        x=0
                        y=0
                    elif y%2==1:
                        self.signal=self.signal[:counter-4]+'000V'+self.signal[counter:]
                        x=0
                        y=0
            elif i == '1':
                x=0
                y+=1
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        temp=0
        for i in self.signal:
            if i == '0':
                self.zero()
            else:
                if i=='1' or i=='B':
                    temp+=1
                elif  i == 'V':
                    temp=temp
                count=temp%2
                if count==1:
                    self.onepos()
                elif count == 0:
                    self.oneneg()

    def zero(self):
        t.sety(self.base)
        t.forward(self.distance)

    def onepos(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def oneneg(self):
        t.sety(self.logic_low)
        t.forward(self.distance)

# Differential Manchester
class diff_Manchester:
    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        prev_num = 2 
        for i in self.signal:
            if i == '0':
                self.pattern(prev_num, '0')
            elif i == '1':
                num = 1 if prev_num == 2 else 2
                self.pattern(num, '1')
                prev_num = num

    def pattern(self, num, write):
        if num == 1:
            t.sety(self.logic_high)
            t.forward(self.distance)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.sety(self.logic_low)
            t.forward(self.distance)
        elif num == 2:
            t.sety(self.logic_low)
            t.forward(self.distance)
            t.sety(self.logic_high)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.forward(self.distance)


def drawAxes():
    def drawLineAndBack(distance):
        for i in range(distance // 50):
            t.forward(50)
            t.dot(5)
        t.backward(distance)

    t.hideturtle()
    t.speed('fastest')
    t.setx(-len_X // 2 + 100)
    drawLineAndBack(len_X)
    t.rt(90)
    drawLineAndBack(100)
    t.rt(180)
    drawLineAndBack(100)
    t.rt(90)


def setTurtle(size, colour, speed, visibility):
    t.pensize(size)
    t.pencolor(colour)
    t.speed(speed)
    if not visibility:
        t.hideturtle()

def randomstring(length):
    samplestring='01'
    result = ''.join((random.choice(samplestring) for x in range(length)))
    return result

def length4string(length):
    samplestring='00001'
    result = ''.join((random.choice(samplestring) for x in range(length)))
    if result.count("0000")>=1:
        return result
    else:
        return length4string(length)

def length8string(length):
    samplestring='000000001'
    result = ''.join((random.choice(samplestring) for x in range(length)))
    if result.count("00000000")>=1:
        return result
    else:
        return length8string(length)

def longestPalindrome(s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]                
        return longest_palindrom

x=input("Select the input method:\n1. Completely Random String\n2. String with fixed Sub-sequences\n3. Completely Manual input\n")
if x=="1":
    size=int(input("Enter the length of string: "))
    signal=randomstring(size)
elif x=="2":
    size=int(input("Enter the length of string: "))
    y=input("Select the number of zeroes:\n1. 4 Zeroes as sub-sequence\n2. 8 Zeroes as sub-sequence\n")
    if y=='1':
        signal=length4string(size)
    elif y=='2':
        signal=length8string(size)
elif x=="3":
    print('Input Signal to be plotted (1s and 0s)')
    signal = input()
print('\nEncode in format:\n1. NRZ-I\n2. NRZ-L\n3. Manchester\n4. Diff Manchester\n5. AMI\n')
encoding = input()
if encoding == '5':
    print('\nEncode in format:\na. AMI(Without Scrambling)\nb. B8ZS\nc. HDB3\n')
    encoding = input()
print("Entered Input :",signal)
root = tk.Tk()
root.title('Signal Graph')
root.geometry('1000x300')
cv = turtle.ScrolledCanvas(root, width=1000)
cv.pack()

len_X, len_Y = 5000, 300
default_settings = (2, 'red', 'fastest', False)
invisiline = (1, 'black', 'fastest', False)
map = {'1': NRZ_I(signal), '2': NRZ_L(signal), '3': Manchester(signal),
       '4': diff_Manchester(signal), 'a':AMI(signal), 'b':B8ZS(signal), 'c':HDB3(signal)}

screen = turtle.TurtleScreen(cv)
screen.screensize(len_X, len_Y)
t = turtle.RawTurtle(screen)

drawAxes()
setTurtle(*default_settings)
map[encoding].draw()
palindrome=longestPalindrome(signal)
print("longest Palindrome:",palindrome)

root.mainloop()

### .................................... Program Ends .................................................... ###