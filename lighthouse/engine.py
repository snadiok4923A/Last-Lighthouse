MORSE={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."," ":"/"}
def decode_morse(signal):
    rev={v:k for k,v in MORSE.items()}
    try: return " ".join("".join(rev[t] for t in word.split()) for word in signal.strip().split(" / "))
    except KeyError as e: raise ValueError(f"Unknown Morse token: {e.args[0]}")
def decode_binary(bits):
    groups=bits.strip().split()
    if not groups or any(len(x)!=8 or set(x)-{"0","1"} for x in groups): raise ValueError("Use 8-bit binary groups separated by spaces.")
    return "".join(chr(int(x,2)) for x in groups)
def decode_caesar(message,shift):
    out=[]
    for c in message:
        if c.isascii() and c.isalpha():
            a=ord("A") if c.isupper() else ord("a"); out.append(chr((ord(c)-a-shift)%26+a))
        else: out.append(c)
    return "".join(out)
def check_answer(user,expected): return " ".join(user.strip().upper().split())==" ".join(expected.strip().upper().split())
def score_answer(correct,streak):
    return (100+min(streak,5)*25,streak+1) if correct else (0,0)
