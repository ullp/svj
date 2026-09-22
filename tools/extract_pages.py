#!/usr/bin/env python3
"""Extract text from Apple .pages files (zip archives) and print .gdoc link files."""
import sys
import zipfile
import re
import xml.etree.ElementTree as ET


def extract_pages(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        # Preferred: index.xml (IWA is snappy, harder); fallback preview.pdf
        if "index.xml" in names:
            data = z.read("index.xml").decode("utf-8", errors="replace")
            text = re.sub(r"<[^>]+>", "\n", data)
            return "\n".join(line for line in (l.strip() for l in text.splitlines()) if line)
        for cand in names:
            if cand.endswith(".pdf"):
                pdf_bytes = z.read(cand)
                tmp = "/tmp/_pages_preview.pdf"
                with open(tmp, "wb") as f:
                    f.write(pdf_bytes)
                from extract_pdf import extract_with_pypdf, extract_raw
                try:
                    return extract_with_pypdf(tmp)
                except Exception:
                    return extract_raw(tmp)
        # IWA fallback: pull printable strings
        out = []
        for cand in names:
            if cand.endswith(".iwa"):
                blob = z.read(cand)
                for m in re.finditer(rb"[\x20-\x7e\xc0-\xff]{6,}", blob):
                    out.append(m.group(0).decode("latin-1"))
        return "\n".join(out)


def main():
    for path in sys.argv[1:]:
        print(f"===== {path} =====")
        try:
            if path.endswith(".pages"):
                print(extract_pages(path))
            else:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
               	 print(f.read())
        except Exception as e:
            print(f"[error: {e}]")


if __name__ == "__main__":
    main()
