import matplotlib.pylab as plt
charOffset = 65

# Counting the frequences of all letters in the ciphertext
def countFrequencies(cipher: str):
    charFrequencies = {}
    for i in range(26):
        char = chr(i + charOffset)
        charFrequencies[char] = cipher.count(char)
    return charFrequencies

# Decryption under given the an affine cipher with a specific key was used
def tryDecryptAffine(chiper: str, key: {"a": int, "b": int}):
    result = ""
    for c in chiper:
        oldValue = ord(c)
        ainv = pow(key["a"], -1, 26)
        newValue = (ainv*((oldValue - charOffset) - key["b"])) % 26 + charOffset
        result = result + chr(newValue)
    result = result.lower()
    return result

def plotFrequencies(charFrequencies):
    lists = sorted(charFrequencies.items())
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.show()

def blockCount(cipher, t):
    cutString = ""
    for i in range(len(cipher)):
        if i % t == 0:
            cutString = cutString + cipher[i]
    return countFrequencies(cutString)

ciphertext1 = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"
ciphertext2 = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"
ciphertext3 = "BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKCGJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBNLHJMBLRFFJELHWEYLWISTFVVYFJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX"

frequencies1 = countFrequencies(cipher=ciphertext1)
frequencies2 = countFrequencies(cipher=ciphertext2)
frequencies3 = countFrequencies(cipher=ciphertext3)
frequencies4 = blockCount(cipher=ciphertext3, t=2)

plain = tryDecryptAffine(chiper=ciphertext1, key={"a": 19, "b": 4})

print(plain)

plotFrequencies(frequencies1)
plotFrequencies(frequencies2)
plotFrequencies(frequencies3)
plotFrequencies(frequencies4)