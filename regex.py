import re

def get_bpm_key (path:str):
    txt = path.split("\\")[-1]

    # \ masks symbol in order to use it in the regex
    w = re.search(r"\[.*\]", txt)
    number = w.group().strip()
    #print(number)

    txt = txt.replace(w.group(), "")

    # \s matches any white space character
    x = re.search(r"\s.*Minor", txt)
    key = x.group().strip()
    #print(key)

    txt = txt.replace(x.group(), "")

    y = re.search(r"\s.*BPM", txt.strip())
    bpm = y.group().strip().replace("BPM", "")
    #print(bpm)

    txt = path.split("\\")[-1]
    #print(txt)

    # (?<={key}) positive lookbehind = beginning of string
    # (?={bpm} positive lookahead = end of string
    z = re.search(fr"(?<=BPM )(.*?)(?= \(Prod)", txt)
    name = z.group().strip()
    #print(name)


    return bpm, key, name

