def vow():
    n=input( )
    list=['a','e','i','o','u']
    llist=['b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    if n in list:
        print("Vowel")
    elif n in llist:
        print("Consonant")
    else:
        print("Invalid")
vow()
