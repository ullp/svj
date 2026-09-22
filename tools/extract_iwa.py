#!/usr/bin/env python3
"""Extract readable text from Pages Document.iwa (snappy-framed protobuf)."""
import struct, sys, zipfile, re, os, tempfile

def snappy_decompress(data):
    # IWA chunk framing (verified empirically): [1B flag/unused][u24 LE length][snappy payload]
    # e.g. hdr 00 17 2b 00 -> length = 0x2b17 = 11031 = len(data)-4.
    out = bytearray()
    pos = 0
    while pos + 4 <= len(data):
        length = int.from_bytes(data[pos + 1:pos + 4], 'little')
        chunk = data[pos + 4:pos + 4 + length]
        if len(chunk) < length:
            break
        out += snappy_raw_decompress(chunk)
        pos += 4 + length
    return bytes(out)

def snappy_raw_decompress(chunk):
    # snappy format: varint uncompressed length, then tags
    def read_varint(buf, i):
        result = 0
        shift = 0
        while True:
            b = buf[i]
            i += 1
            result |= (b & 0x7f) << shift
            if not (b & 0x80):
                return result, i
            shift += 7
    n, i = read_varint(chunk, 0)
    out = bytearray()
    while i < len(chunk):
        tag = chunk[i]
        i += 1
        t = tag & 0x03
        if t == 0:
            N = tag >> 2
            if N < 60:
                length = N + 1
            else:
                nb = N - 59  # 60..63 -> 1..4 length bytes, little-endian, value = len-1
                length = int.from_bytes(chunk[i:i + nb], 'little') + 1
                i += nb
            out += chunk[i:i + length]
            i += length
        elif t == 1:
            # copy, 1-byte offset: len in [4..11] = ((tag>>2)&7)+4; 11-bit offset
            length = ((tag >> 2) & 0x07) + 4
            offset = ((tag >> 5) << 8) | chunk[i]
            i += 1
            src = len(out) - offset
            if src < 0:
                raise ValueError('bad copy1')
            for k in range(length):
                out.append(out[src + k])
        elif t == 2:
            # copy, 2-byte offset: len in [1..64] = (tag>>2)+1; 16-bit LE offset
            length = (tag >> 2) + 1
            offset = int.from_bytes(chunk[i:i + 2], 'little')
            i += 2
            src = len(out) - offset
            if src < 0:
                raise ValueError('bad copy2')
            for k in range(length):
                out.append(out[src + k])
        else:
            # copy, 4-byte offset: len = (tag>>2)+1; 32-bit LE offset
            length = (tag >> 2) + 1
            offset = int.from_bytes(chunk[i:i + 4], 'little')
            i += 4
            src = len(out) - offset
            if src < 0:
                raise ValueError('bad copy4')
            for k in range(length):
                out.append(out[src + k])
    if len(out) != n:
        raise ValueError('length mismatch: got %d, expected %d' % (len(out), n))
    return bytes(out)

def extract(path):
    with zipfile.ZipFile(path) as z:
        data = z.read('Index/Document.iwa')
    raw = snappy_decompress(data)
    # extract valid UTF-8 text runs (protobuf field tags interrupt them)
    texts = re.findall(
        rb'(?:[\x20-\x7e]|[\xc2-\xdf][\x80-\xbf]|[\xe0-\xef][\x80-\xbf]{2}|[\xf0-\xf4][\x80-\xbf]{3}){4,}',
        raw)
    res = []
    for t in texts:
        try:
            s = t.decode('utf-8')
        except UnicodeDecodeError:
            continue
        if len(s.strip()) >= 4 and re.search(r'[A-Za-zÁ-Žá-ž]', s):
            res.append(s.strip())
    return res

if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('===== ' + os.path.basename(p) + ' =====')
        try:
            for s in extract(p):
                print(s)
        except Exception as e:
            print('ERROR', e)
