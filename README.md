# shepherd
Globe scanner

Requirements:  
    - any vpn connection  
    - zmap  
    - zgrab  
    - https://github.com/gushitong/libzmap  
    - pip  
    - setuptools  

Description:  
Scanning the net block of every country for open ports 80,443,22,21,3384  

Workflow:  
1. Connect to VPN
2. Get CIDR list per country
3. Scan countries for ports
4. Save to disk
5. Analyze results
6. Report analysis

Requirements to workflow:
1. VPN -> mullvad  
    a. no DNS leaks  
    b. long running VPN  
    c. moderate bandwidth
2. CIDR  
    a. update every scan
    b. optimize speed
3. Scan  
    a. maximize speed
4. Save  
    a. keep past results for 3+ years  
    b. maximize disk usage  
    c. Host, Country, DNS, Industry, Owner  
5. Analyze  
    a. Change over time + current state  
    b. per host  
    c. per CIDR  
    d. Country  
    e. Global  
    f. React

