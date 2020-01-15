#!/usr/bin/env python3
import cgi
import os
import html

def header():
    print("Content-type: text/plain")
    print()
def main():
    params = cgi.FieldStorage()
    header()
    print(str(len(params)))
    print(html.escape(os.environ["REMOTE_ADDR"]))

if __name__ == "__main__":
    main()