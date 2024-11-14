#### Fonction secondaire
""" test si un mot ou une phrase est palindrome"""

def ispalindrome(p):
    """ return faux si le mot n'est pas un palindrome"""
    table = str.maketrans("éèêëàôç","eeeeaoc", " ',-!?:") ###  traduction cas avec accent
    p = p.lower() ### tranformer chaine de carac en minuscule
    p = p.translate(table) ### changer tt les carac avec accent en carac sans accent
    l = len(p)
    if p[::1]==p[-1:-l-1:-1] : ### mot a l'endroit different du  mot a l'envers
        return True

    return False

#### Fonction principale


def main():
    """ test de la fonction secondaire"""
    print("bonbon", ispalindrome("bonbon"))# vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
