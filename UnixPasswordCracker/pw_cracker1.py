__author__ = 'kaya'
import crypt
def testPass(cryptPass, dname):
    salt = cryptPass[0:2]
    dictFile = open(dname, 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print("Found Password: " + word + "\n")
            return
    print("Password not Found")
    return

def main():
    passFile = open('password.txt', 'r')
    for line in passFile.readlines():
        user = line.split(":")[0]
        #print(line)
        cryptPass = line.split(':')[1].strip(' ')
        print("crypted: " + cryptPass)
        print("Cracking Password For: " + user)
        testPass(cryptPass, "dictionary.txt")


if __name__ == "__main__":
    main()