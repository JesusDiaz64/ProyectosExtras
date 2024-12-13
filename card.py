

def isvalid(n):
    t = 0
    for x, y in enumerate(reversed(n)):
        y = int(y)
        if x%2 == 1:
            y = y * 2
            if y >= 10:
                t += y // 10 + y%10
            else:
                t+=y
        else:
            t+=y
    return t%10 == 0

def cardtype(n):
    a = int(n[0])
    b = int(n[0:2])
    l = len(n)
    
    if l == 15 and (b == 34 or b == 37):
        return '**AMERICAN EXPRESS'
    if l == 16 and 51 <= b <= 55:
        return '**MASTERCARD'
    if l in [13, 16] and a == 4:
        return '**VISA'
    if l == 16 and b in [60, 62, 64, 65]:
        return '**DISCOVER'
    return 'NONE--'

NC = "4152313900047783"

while NC!='0':
    NC = input("Enter credit card#: ")
    
    if not NC.isdigit():
        print("Invalid input. Please enter only numeric values.")
        continue
    
    if isvalid(NC):
        print("Is Valid!,  type: ",cardtype(NC))
    else:
        print("Invalid...")
    
        