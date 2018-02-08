with open('filename.txt', 'r') as myfile:
    source=myfile.read().replace('\n', '')

def run(src):
    c = [0] * 30000
    p = 0
    loop = []
    rv = []
    ts = list(src)
    l = len(ts)
    i = 0
    while i < l:
        t = ts[i]
        if t == ">": p += 1
        elif t == "<": p -= 1
        elif t == "+": c[p] += 1
        elif t == "-": c[p] -= 1
        elif t == ".": rv.append(chr(c[p]))
        elif t == ",": pass
        elif t == "[":
            if c[p] == 0:
                while ts[i] != "]": i += 1
                loop.pop()
            else:
                loop.append(i - 1)
        elif t == "]": i = loop[-1]
        i += 1

    print("".join(rv))

def parse_source():
    run(source)

if __name__ == "__main__":
    parse_source()
    
    

