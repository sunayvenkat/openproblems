# crude PDF text extractor: inflate streams, pull strings from TJ/Tj.
# shortcut: no font encodings/CMaps, math will be garbled; fine for reading prose of LaTeX papers.
import re, sys, zlib
data = open(sys.argv[1], 'rb').read()
BS = b'\x5c'
out = []
for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.S):
    s = m.group(1)
    try:
        s = zlib.decompress(s)
    except Exception:
        continue
    if b'BT' not in s:
        continue
    line = []
    i = 0
    # tokenize strings (...) with escapes, arrays, numbers, operators
    n = len(s)
    while i < n:
        c = s[i:i+1]
        if c == b'(':
            depth = 1; j = i + 1; buf = bytearray()
            while j < n and depth:
                ch = s[j:j+1]
                if ch == BS:
                    nx = s[j+1:j+2]
                    if nx and nx in b'01234567':
                        k = j + 1; oc = b''
                        while k < n and len(oc) < 3 and s[k:k+1] in b'01234567':
                            oc += s[k:k+1]; k += 1
                        buf.append(int(oc, 8) & 255); j = k; continue
                    buf += {b'n': b'\n', b'r': b'', b't': b' '}.get(nx, nx); j += 2; continue
                if ch == b'(':
                    depth += 1
                elif ch == b')':
                    depth -= 1
                    if depth == 0:
                        break
                buf += ch; j += 1
            line.append(bytes(buf)); i = j + 1; continue
        mnum = re.match(rb'-?\d+\.?\d*', s[i:i+20])
        if mnum and c in b'-0123456789.':
            if float(mnum.group(0)) < -250 and line and line[-1] != b' ':
                line.append(b' ')
            i += len(mnum.group(0)); continue
        mop = re.match(rb'(T\*|Td|TD|Tm|ET)\b', s[i:i+3])
        if mop:
            line.append(b'\n'); i += len(mop.group(0)); continue
        i += 1
    t = b''.join(line)
    t = re.sub(rb'\n\s*\n+', b'\n', t)
    out.append(t.decode('latin-1'))
sys.stdout.write('\n'.join(out))
