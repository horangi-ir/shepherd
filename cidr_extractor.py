import math
import urllib

arin = 'ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest'
ripe = 'ftp://ftp.ripe.net/ripe/stats/delegated-ripencc-latest'
afrinic = 'ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-latest'
apnic = 'ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-latest'
lacnic = 'ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-latest'


def queryRegistrar(countryAbbreviation, registrar):
    opener = urllib.FancyURLopener()
    f = opener.open(registrar)
    lines=f.readlines()
    netblocks = []
    ip = ""
    for line in lines:
            if (('ipv4' in line) & (countryAbbreviation in line)) :
                    s=line.split("|")
                    net=s[3]
                    cidr=float(s[4])
                    ip = "%s/%d" % (net,(32-math. log(cidr,2)))
                    netblocks.append(ip)

    return netblocks

def getIps(countryAbbreviation):
    ips = queryRegistrar(countryAbbreviation, apnic)

    return ips
