""" Morse code converter and player  source of lists https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php"""
import time
import winsound as ws
f = 2500 #frequency

switcher = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    ' ' : ' ',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
    ',' : '--..--',
    '?' : '..--..',
    ':' : '---...',
    '-' : '-....-',
    '"' : '.-..-.',
    '(' : '-.--.',
    '=' : '-...-',
    '*' : '-..-',
    '.' : '.-.-.-',
    ';' : '-.-.-.',
    '/' : '-..-.',
    '\'' : '.----.',
    '_' : '..--.-',
    ')' : '-.--.-',
    '+' : '.-.-',
    '@' : '.--.-.',
}

def player(s):
    for i in s:
        print(' ',end='')
        play(i)

def play(w):
    w = switcher.get(w,None)
    for i in w:
        if i == '.':
            print('.',end='')
            ws.Beep(f,150)
        if i == '-':
            print('-',end='')
            ws.Beep(f,400)
        if i == ' ':
            print('   ',end='')
            time.sleep(0.6)
            continue
        time.sleep(0.5)


def converter(s,flag):
    output = ''
    for i in s:
        if i == ' ':
            output += ' '
        output += ' ' + switcher.get(i,None)
    print('OUTPUT - :')
    print(output)
    if flag:
        print('playing your string...')
        player(s)



print('1.) Enter string to play it : INPUT = 1 ')
print('1.) Enter string to convert it : INPUT = 2 ')
n = input()
if n == '1':
    string = input('Type your String : ')
    player(string)
if n == '2':
    string = input('Type your string : ')
    j = input('Do you want to play it too ? (y/n) : ')
    if j == 'y':
        converter(string,True)
    if j == 'n':
        converter(string,False)

