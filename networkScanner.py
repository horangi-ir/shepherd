from libzmap import ZmapProcess
import json
import sys
from cidr_extractor import getIps

testList1 = ['221.128.100.0/22']

sg = getIps('SG')

def scanner(ipList):
    scan = []
    for i in ipList:
        print i
        proc = ZmapProcess(targets=i, options='-B 100M', probe_module='icmp_echoscan', port='80')
        for obj in proc.run():
            print obj.saddr


if __name__ == "__main__":
    scanner(sg)