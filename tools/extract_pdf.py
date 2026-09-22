#!/usr/bin/env python3
"""Extract text from PDF files. Tries several libraries, falls back to raw stream decode."""
import sys
import zlib
import re


def extract_with_pypdf(path):
    from pypdf import PdfReader
    reader = PdfReader(path)
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def extract_with_pypdf2(path):
    from PyPDF2 import PdfReader
    reader = PdfReader(path)
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def extract_with_fitz(path):
    import fitz
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def extract_raw(path):
    with open(path, "rb") as f:
        data = f.read()
    texts = []
    for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", data, re.S):
        chunk = m.group(1)
        try:
            chunk = zlib.decompress(chunk)
        except Exception:
            continue
        # Extract text from Tj / TJ operators
        for tm in re.finditer(rb"\((?:[^()\\]|\\.)*\)", chunk):
            s = tm.group(0)[1:-1]
            s = s.replace(b"\\(", b"(").replace(b"\\)", b")").replace(b"\\\\", b"\\")
            try:
                texts.append(s.decode("utf-8"))
            except UnicodeDecodeError:
                try:
                    texts.append(s.decode("cp1250"))
                except UnicodeDecodeError:
                    texts.append(s.decode("latin-1"))
    return " ".join(texts)


def main():
    for path in sys.argv[1:]:
        print(f"===== {path} =====")
        for fn in (extract_with_pypdf, extract_with_pypdf2, extract_with_fitz, extract_raw):
            try:
                text = fn(path)
                if text and text.strip():
                    print(text)
                    break
            except Exception as e:
                print(f"[{fn.__name__} failed: {e}]", file=sys.stderr)
        else:
            print("[no text extracted]")


if __name__ == "__main__":
    main()
