from question_d import get_profiles, get_consensus

store_dna = "n"

print("Welcome to my DNA Program")
stored_dna = input("Would you like to read DNA Strings from prepared DNA File? Y or N?")
dna_file = open("dnas.txt", "r")
counter = 7
while stored_dna.lower() == "y":
    dna1 = dna_file.readline().rstrip("\n")
    print(dna1, "- There are", counter, "records left in this file")
    counter -= 1
    if counter >= 0:
        stored_dna = input("Would you like to pull a DNA String from prepared DNA File? Y or N?")
    else:
        break
dna_file.seek(0)
dna_strings=print("Now taking all DNA Strings from file and rendering your profile list")
dna0 = dna_file.readline()
dna1 = dna_file.readline()
dna2 = dna_file.readline()
dna3 = dna_file.readline()
dna4 = dna_file.readline()
dna5 = dna_file.readline()
dna6 = dna_file.readline()
dna7 = dna_file.readline()
profile_list = get_profiles(dna0, dna1, dna2, dna3, dna4, dna5, dna6, dna7)
print("Your rendered profile list is:", profile_list)

print("Now rendering your profile concensus based on your rendered profile list")
dna_concensus = get_consensus(profile_list)
print("Your rendered DNA Concensus is", dna_concensus)
print("Thank you for running this DNA Program")


