import nmap
import sys
nmScan = nmap.PortScanner()
# ipList = ['61.247.43.165','61.247.43.164','61.247.43.163']
# for i in ipList:
nmScan.scan('127.0.0.1', '0-1023')
for port in nmScan['127.0.0.1']['tcp']:
    thisDict = nmScan['127.0.0.1']['tcp'][port]
    print 'Port ' + str(port) + ': ' + thisDict['product'] + ', v' + thisDict['version']


if __name__ == "__main__":
    pass