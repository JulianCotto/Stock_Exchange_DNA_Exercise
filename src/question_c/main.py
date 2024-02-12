from question_c import get_most_likey_ancenstor_consensus


print("Welcome to the DNA Program")

def main():
    run_again = "y"

    while run_again.lower() == "y": 
        dna_string1 = input("Please enter a DNA String at least 8 characters in length and no longer than 16 characters in length")
        while len(dna_string1) < 8 or len(dna_string1) > 16:
            print("Invalid Entry, DNA String MUST BE between 8 and 16 characters in length.")
            dna_string1 = input("Please enetr a DNA String at least 8 characters in length and no longer than 16 characters in length")
        dna_string2 = input("Please enter a DNA sequence that is EXACTLY 4 characters in length")
        while len(dna_string2) != 4:
            print("Invalid Entry, DNA String MUST BE exactly 4 characters in length")
            dna_string2 = input("Please enter a DNA sequence that is EXACTLY 4 characters in length")
        print("Now Calculating Most Likely Ancestor")
        Most_likely = get_most_likey_ancenstor_consensus(dna_string1, dna_string2)
        if len(Most_likely) > 0:
            print("I have found", len(Most_likely), "matches within the provided DNA Strings! They are", Most_likely)
        elif len(Most_likely) == 1:
            print("I have found 1 match within the provided DNA Strings! It is", Most_likely)
        else:
            print("There were no matches within the provided DNA Strings")

        
        run_again = input("Do you want to run this program again? Y or N")
        while run_again.lower() == "y":
            main()
        else:
            print("Thank you for running the program")
            quit()
        
main()
