def binToDec(bin:str)->str:
    x = 0
    bin_inv = list(str(bin))[::-1]
    e = 0
    for i in bin_inv:
        x+= int(i)*2**e
        e+=1
    return str(x)

def decToBin(dec:str)->str:
    dec = int(dec)
    bin = []
    while dec != 0:
        bin.append(dec % 2)
        dec = dec//2
    bin = bin[::-1]
    b = ''
    for i in bin:
        b += str(i)
    return b

def decToHex(dec:str)->str:
    dec = int(dec)
    H = {0: '0',1: '1',2: '2',3: '3', 4: '4',5: '5',6: '6',7: '7',8: '8',9: '9',10: 'A',11: 'B',12: 'C',13: 'D',14: 'E',15: 'F'}
    hex = []
    while dec != 0:
        a = dec%16
        hex.append(H[a])
        dec = dec // 16
    hex = hex[::-1]
    b = ''
    for i in hex:
        b += str(i)
    return b
def hexToDec(hex:str)->str:
    x = 0
    e = 0
    H = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex = list(hex)[::-1]
    for i in hex:
        x += int(H[i]) * 16 ** e
        e += 1
    return str(x)

def hexToBin(hex: str) ->str:
    dec = hexToDec(hex)
    bin = decToBin(dec)
    return bin

def binToHex(bin:str)->str:
    dec = binToDec(bin)
    hex = decToHex(dec)
    return hex

def octToDec(oct: str) ->str:
    x = 0
    e = 0
    H = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
    oct = list(str(oct))[::-1]
    for i in oct:
        x += int(H[i]) * 8 ** e
        e += 1
    return str(x)

def decToOct(dec: str) ->str:
    H = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}
    oct = []
    dec = int(dec)
    while dec != 0:
        a = dec % 8
        oct.append(H[a])
        dec = dec // 8
    oct = oct[::-1]
    b = ''
    for i in oct:
        b += str(i)
    return b
def octToBin(oct):
    dec = octToDec(oct)
    bin = decToBin(dec)
    return bin

def binToOct(bin):
    dec = binToDec(bin)
    oct = decToOct(dec)
    return oct

def hexToOct(hex):
    dec = hexToDec(hex)
    oct = decToOct(dec)
    return oct

def octToHex(oct):
    dec = octToDec(oct)
    hex = decToHex(dec)
    return hex