import json
from pathlib import Path
from .engine import decode_morse,decode_binary,decode_caesar,check_answer,score_answer
SAVE=Path(__file__).resolve().parent.parent/"lighthouse_save.json"
PUZZLES=[
{"chapter":"01 · THE FOG","story":"A storm swallows the coast. A weak lamp flickers from the old lighthouse.","type":"MORSE","signal":"... --- ...","hint":"Three short, three long, three short: a famous distress call.","answer":"SOS","note":"Morse code represents letters with short dots and long dashes."},
{"chapter":"02 · THE AUTOMATON","story":"A brass keeper-bot wakes. Its memory is stored in eight-bit groups.","type":"BINARY","signal":"01000111 01001111 01001111 01000100","hint":"Convert each 8-bit group from base 2 to an ASCII character.","answer":"GOOD","note":"ASCII maps numeric codes to text characters."},
{"chapter":"03 · THE OLD MAP","story":"A map is locked behind a message shifted three letters forward.","type":"CAESAR","signal":"WKH NHB LV XQGHU WKH ODPS","shift":3,"hint":"Move each letter three places backward in the alphabet.","answer":"THE KEY IS UNDER THE LAMP","note":"A Caesar cipher shifts each alphabet letter by a fixed number."},
{"chapter":"04 · THE DEEP","story":"A ship answers from the darkness. Its message arrives in hexadecimal.","type":"HEX","signal":"4E 4F 52 54 48","hint":"Each pair is a hexadecimal ASCII byte. 4E is the letter N.","answer":"NORTH","note":"Hexadecimal uses base 16 and is a compact way to write bytes."},
{"chapter":"05 · THE FINAL BEACON","story":"The lens is aligned. One final message will guide every ship home.","type":"MORSE","signal":"..-. --- .-.. .-.. --- .-- / - .... . / .-.. .. --. .... -","hint":"Decode the Morse words. A slash separates words.","answer":"FOLLOW THE LIGHT","note":"Morse code can carry full messages, not just emergency calls."}
]
def decode_hex(s):
    try:return bytes.fromhex(s).decode("ascii")
    except (ValueError,UnicodeDecodeError) as e:raise ValueError("Invalid hexadecimal ASCII signal.") from e
def decode_puzzle(p):
    return {"MORSE":lambda:decode_morse(p["signal"]),"BINARY":lambda:decode_binary(p["signal"]),"CAESAR":lambda:decode_caesar(p["signal"],p["shift"]),"HEX":lambda:decode_hex(p["signal"])}[p["type"]]()
def best_score():
    try:return int(json.loads(SAVE.read_text()).get("best_score",0))
    except (OSError,ValueError,TypeError):return 0
def play():
    print("\n"+"="*54+"\n          THE LAST LIGHTHOUSE\n      A signal-decoding adventure\n"+"="*54)
    print("Five transmissions. One storm. Bring the coast back to life.")
    print("Personal best:",best_score()); input("Press Enter to begin...")
    score=streak=0
    for i,p in enumerate(PUZZLES):
        print("\n"+"-"*54+"\n"+p["chapter"]+"\n"+p["story"])
        print("\nINCOMING",p["type"],"SIGNAL:\n ",p["signal"])
        while True:
            a=input("> ").strip()
            if a.upper()=="QUIT": print("The beacon fades. Run again to restart."); return
            if a.upper()=="HINT": print("CLUE:",p["hint"]); continue
            if check_answer(a,p["answer"]):
                points,streak=score_answer(True,streak); score+=points
                print(f"Decoded! +{points} points | streak x{streak}\nFIELD NOTE:",p["note"]); break
            streak=0; print("Not quite. Try again, or type HINT.")
        if i<len(PUZZLES)-1:input("Press Enter for next transmission...")
    record=max(score,best_score()); SAVE.write_text(json.dumps({"best_score":record},indent=2))
    print("\nTHE LIGHTHOUSE IS ALIVE!\nFinal score:",score,"| Best score:",record)
    print("You explored Morse, binary, ASCII, hexadecimal and Caesar ciphers.")
