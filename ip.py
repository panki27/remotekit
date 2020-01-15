#!/usr/bin/env python3
import cgi
import os
import html

F_PLAIN = 0
F_XML = 1
F_JSON = 2

def header():
    print("Content-type: text/plain")
    print()
def main():
    params = cgi.FieldStorage()
    out = {
      "ip": None
    }
    header()
    remote_ip = html.escape(os.environ["REMOTE_ADDR"])
    format = F_PLAIN
    if(len(params) > 0):
        for key in params:
            if key == "format":
                r_format = params[key].value
                if r_format == "xml":
                    format = F_PLAIN
                    print("lol xml are you serious? get with the times")
                elif r_format == "json":
                    format = F_JSON

    out["ip"] = remote_ip
    for item in out:
        if format == F_PLAIN:
            print(out[item])
        elif format == F_JSON:
            import json
            print(json.dumps(out))
if __name__ == "__main__":
    main()