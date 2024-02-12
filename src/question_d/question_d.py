import string


def get_profiles(dna0, dna1, dna2, dna3, dna4, dna5, dna6, dna7):
    indna0 = list(dna0)
    indna1 = list(dna1)
    indna2 = list(dna2)
    indna3 = list(dna3)
    indna4 = list(dna4)
    indna5 = list(dna5)
    indna6 = list(dna6)
    indna7 = list(dna7)
    
    i = 0
    acounter = 0
    gcounter = 0
    ccounter = 0
    tcounter = 0
    for i in range(len(indna0)):
        if indna0[i] == "A":
            acounter += 1
        elif indna0[i] == "C":
            ccounter += 1
        elif indna0[i] == "G":
            gcounter += 1
        elif indna0[i] == "T":
            tcounter += 1
        i += 1

    A0 = acounter
    C0 = ccounter
    G0 = gcounter
    T0 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna1)):
        if indna1[i] == "A":
            acounter += 1
        elif indna1[i] == "C":
            ccounter += 1
        elif indna1[i] == "G":
            gcounter += 1
        elif indna1[i] == "T":
            tcounter += 1
        i += 1
        
    A1 = acounter
    C1 = ccounter
    G1 = gcounter
    T1 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna2)):
        if indna2[i] == "A":
            acounter += 1
        elif indna2[i] == "C":
            ccounter += 1
        elif indna2[i] == "G":
            gcounter += 1
        elif indna2[i] == "T":
            tcounter += 1
        i += 1
        
    A2 = acounter
    C2 = ccounter
    G2 = gcounter
    T2 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna3)):
        if indna3[i] == "A":
            acounter += 1
        elif indna3[i] == "C":
            ccounter += 1
        elif indna3[i] == "G":
            gcounter += 1
        elif indna3[i] == "T":
            tcounter += 1
        i += 1
        
    A3 = acounter
    C3 = ccounter
    G3 = gcounter
    T3 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna4)):
        if indna4[i] == "A":
            acounter += 1
        elif indna4[i] == "C":
            ccounter += 1
        elif indna4[i] == "G":
            gcounter += 1
        elif indna4[i] == "T":
            tcounter += 1
        i += 1
        
    A4 = acounter
    C4 = ccounter
    G4 = gcounter
    T4 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna5)):
        if indna5[i] == "A":
            acounter += 1
        elif indna5[i] == "C":
            ccounter += 1
        elif indna5[i] == "G":
            gcounter += 1
        elif indna5[i] == "T":
            tcounter += 1
        i += 1
        
    A5 = acounter
    C5 = ccounter
    G5 = gcounter
    T5 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna6)):
        if indna6[i] == "A":
            acounter += 1
        elif indna6[i] == "C":
            ccounter += 1
        elif indna6[i] == "G":
            gcounter += 1
        elif indna6[i] == "T":
            tcounter += 1
        i += 1
        
    A6 = acounter
    C6 = ccounter
    G6 = gcounter
    T6 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    for i in range(len(indna7)):
        if indna7[i] == "A":
            acounter += 1
        elif indna7[i] == "C":
            ccounter += 1
        elif indna7[i] == "G":
            gcounter += 1
        elif indna7[i] == "T":
            tcounter += 1
        i += 1
        
    A7 = acounter
    C7 = ccounter
    G7 = gcounter
    T7 = tcounter
    acounter = 0
    ccounter = 0
    gcounter = 0
    tcounter = 0

    profilea = [A0, A1, A2, A3, A4, A5, A6, A7]
    profilec = [C0, C1, C2, C3, C4, C5, C6, C7]
    profileg = [G0, G1, G2, G3, G4, G5, G6, G7]
    profilet = [T0, T1, T2, T3, T4, T5, T6, T7]
    profiles_list = [profilea, profilec, profileg, profilet]

    return profiles_list

def get_consensus(profiles_list):
    profilea = profiles_list[0]
    profilec = profiles_list[1]
    profileg = profiles_list[2]
    profilet = profiles_list[3]

    max0 = max(profilea[0], profilec[0], profileg[0], profilet[0])
    if max0 == profilea[0]:
        new_max0 = "A"
    elif max0 == profilec[0]:
        new_max0 = "C"
    elif max0 == profileg[0]:
        new_max0 = "G"
    elif max0 == profilet[0]:
        new_max0 = "T"

    max1 = max(profilea[1], profilec[1], profileg[1], profilet[1])
    if max1 == profilea[1]:
        new_max1 = "A"
    elif max1 == profilec[1]:
        new_max1 = "C"
    elif max1 == profileg[1]:
        new_max1 = "G"
    elif max1 == profilet[1]:
        new_max1 = "T"

    max2 = max(profilea[2], profilec[2], profileg[2], profilet[2])
    if max2 == profilea[2]:
        new_max2 = "A"
    elif max2 == profilec[2]:
        new_max2 = "C"
    elif max2 == profileg[2]:
        new_max2 = "G"
    elif max2 == profilet[2]:
        new_max2 = "T"

    max3 = max(profilea[3], profilec[3], profileg[3], profilet[3])
    if max3 == profilea[3]:
        new_max3 = "A"
    elif max3 == profilec[3]:
        new_max3 = "C"
    elif max3 == profileg[3]:
        new_max3 = "G"
    elif max3 == profilet[3]:
        new_max3 = "T"
    
    max4 = max(profilea[4], profilec[4], profileg[4], profilet[4])
    if max4 == profilea[4]:
        new_max4 = "A"
    elif max4 == profilec[4]:
        new_max4 = "C"
    elif max4 == profileg[4]:
        new_max4 = "G"
    elif max4 == profilet[4]:
        new_max4 = "T"
        
    max5 = max(profilea[5], profilec[5], profileg[5], profilet[5])
    if max5 == profilea[5]:
        new_max5 = "A"
    elif max5 == profilec[5]:
        new_max5 = "C"
    elif max5 == profileg[5]:
        new_max5 = "G"
    elif max5 == profilet[5]:
        new_max5 = "T"

    max6 = max(profilea[6], profilec[6], profileg[6], profilet[6])
    if max6 == profilea[6]:
        new_max6 = "A"
    elif max6 == profilec[6]:
        new_max6 = "C"
    elif max6 == profileg[6]:
        new_max6 = "G"
    elif max6 == profilet[6]:
        new_max6 = "T"

    max7 = max(profilea[7], profilec[7], profileg[7], profilet[7])
    if max7 == profilea[7]:
        new_max7 = "A"
    elif max7 == profilec[7]:
        new_max7 = "C"
    elif max7 == profileg[7]:
        new_max7 = "G"
    elif max7 == profilet[7]:
        new_max7 = "T"

    concensus = [new_max0, new_max1, new_max2, new_max3, new_max4, new_max5, new_max6, new_max7]

    return concensus