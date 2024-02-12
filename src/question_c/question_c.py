def get_most_likey_ancenstor_consensus(dna_string1, dna_string2):
    dna_list = []
    g = len(dna_string2)
    for i in range (len(dna_string1)):
        i += 1
        g += 1
        if dna_string1[i:g] == dna_string2:
            locations = dna_string1.index(dna_string2, i, g)
            locations += 1
            dna_list.append(locations)
        dna_file = open("loc_file.txt", "w")
        dna_file.write(str(dna_list))
        dna_file.close()

    new_dna = open("loc_file.txt", "r")
    cool_dna = new_dna.readline()
    new_cool_dna = cool_dna.lstrip("[").rstrip("]").split(",")
    return new_cool_dna
