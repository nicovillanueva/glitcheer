JPGHEADER = b'\xff\xd8\xff\xe0\x00\x10JFIF'         # 10 bytes
PNGHEADER = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'  # 16 bytes

def detect_format(filepath):
    with open(filepath, 'rb') as f:
        byts = f.read(16)
    if byts[:10] == JPGHEADER:
        return "jpg"
    elif byts[:16] == PNGHEADER:
        return "png"
    else:
        return "dunno"

def print_formats():
    import os, pprint
    r = {}
    bytestoread = 16
    folder = 'samples'
    for fp in os.listdir(folder):
        p = os.path.join(folder, fp)
        with open(p, 'rb') as f:
            ext = p[p.rfind('.')+1:]
            if ext not in r.keys():
                r[ext] = {}
            by = f.read(bytestoread)
            r[ext][fp] = by
        guessed = detect_format(p)
        print("Path: {p}, guessed: {g}".format(p=fp, g=guessed))
    pprint.pprint(r)
