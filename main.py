#!/usr/bin/python
import http.server.*

def listRokus():
    req = HTTPConnection("239.255.255.250", 1900)
    req.request("M-SEARCH", "*", headers = {"Host": "239.255.255.250:1900", "Man": "ssdp:discover", "ST": "roku:ecp"})
    req.
