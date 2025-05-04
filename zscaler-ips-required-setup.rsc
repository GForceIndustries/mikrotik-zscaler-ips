/system script
add dont-require-permissions=yes name=zscaler-ips owner=admin policy=ftp,read,write,test source=":log info \"Download Zscaler IP list\";\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-zscaler-ips/refs/heads/main/zscaler-ips-required-v4.rsc\" mode=https dst-path=zscaler-ips-required-v4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-zscaler-ips/refs/heads/main/zscaler-ips-required-v6.rsc\" mode=https dst-path=zscaler-ips-required-v6.rsc;\r\
    \n\r\
    \n:log info \"Remove current Zscaler IPs\";\r\
    \n/ip firewall address-list remove [find where list=\"zscaler-ips-ipv4\"];\r\
    \n/ipv6 firewall address-list remove [find where list=\"zscaler-ips-ipv6\"];\r\
    \n:log info \"Import newest Zscaler IPs\";\r\
    \n/import file-name=zscaler-ips-required-v4.rsc;\r\
    \n/import file-name=zscaler-ips-required-v6.rsc;"
/system scheduler
add interval=1d name=zscaler-ips on-event=zscaler-ips policy=ftp,read,write,test start-date=2025-04-23 start-time=06:45:00
