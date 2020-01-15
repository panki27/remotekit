#!/usr/bin/env python
import cgi
import os
#import html

F_PLAIN = 0
F_XML = 1
F_JSON = 2

def header():
    print("Content-type: text/plain")
    print("")
def main():
    params = cgi.FieldStorage()
    out = {
      "ip": None,
      "country": None,
      "continent": None,
      "location": None
    }
    header()
    out["ip"] = cgi.escape(os.environ["REMOTE_ADDR"])
    format = F_PLAIN
    if(len(params) > 0):
        for key in params:
            if key == "format":
                r_format = params[key].value
                if r_format == "xml":
                    print("lol xml are you serious? get with the times")
                elif r_format == "json":
                    format = F_JSON
            elif key == "and":
                extras = params[key].value.split(',')
                if "geo" in extras:
                    from geoip import geolite2
                    match = geolite2.lookup(out["ip"].encode("UTF-8"))
                    if match is not None:
                        out["country"] = match.country
                        out["continent"] = match.continent
                        out["location"] = match.location


    if format == F_PLAIN:
        for item in out:
            if out[item] is not None:
                print(out[item])
    elif format == F_JSON:
        import json
        print(json.dumps(dict((k, v) for k, v in out.items() if v is not None)))
if __name__ == "__main__":
    main()