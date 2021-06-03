

def add_detector(message):
    mL = [] 
    cL = []
    iL = [] 
    pL = []
    cS = "" 
    iS = ""
    pS = ""

    for a in message:
        mL.append(a)
    i = 0
    while True:
        if mL[i] == ';':
            break
        cL.append(mL[i])
        i = i+1
    
    for a in range(0, len(cL)+1):
        del mL[0]
    i = 0
    while True:
        if mL[i] == ';':
            break
        iL.append(mL[i])
        i = i + 1
    for a in range(0, len(iL)+1):
        del mL[0]
    pL = mL

    for a in cL:
        cS = cS + a
    for a in iL:
        iS = iS + a
    for a in pL:
        pS = pS + a
    
    print(cS + " to " + iS + ":" + pS)

    
