# Zscaler Hub IP Address Lists for MikroTik Firewalls

MikroTik firewall address lists for Zscaler Hub IPv4 and IPv6 required and recommended address ranges. Refreshed daily at 05:30 UTC. The generated configuration files create IPv4 and IPv6 address lists named **zscaler-ips-ipv4** and **zscaler-ips-ipv6** which can be used in firewall filter/NAT/mangle rules. Lists are generated for both the **required** and **recommended** IP ranges published by Zscaler. You are advised to use the **recommended** lists unless you specifically need to reduce the number of IP ranges permitted. All of the IP ranges in the **required** lists are included in the **recommended** lists; you don't need to configure both.

## Usage 
Create a script to download either **zscaler-ips-recommended-v4.rsc** and **zscaler-ips-recommended-v6.rsc**, or **zscaler-ips-required-v4.rsc** and **zscaler-ips-required-v6.rsc**, remove any existing entries in the **zscaler-ips-ipv4** and **zscaler-ips-ipv6** address lists, and import the new address lists. Then, create a schedule to run the script at an appropriate time for your environment. You can either configure these manually, or download and import either **zscaler-ips-recommended-setup.rsc** or **zscaler-ips-required-setup.rsc** to create them automatically. Read on for a sample script and schedule if you want to configure these manually. If you create the script and schedule manually, they require **ftp**, **read**, **write** and **test** permissions.

### Sample Script

```
:log info "Download Zscaler IP list";
/tool fetch url="https://raw.githubusercontent.com/GForceIndustries/mikrotik-zscaler-ips/refs/heads/main/zscaler-ips-recommended-v4.rsc" mode=https dst-path=zscaler-ips-recommended-v4.rsc;
/tool fetch url="https://raw.githubusercontent.com/GForceIndustries/mikrotik-zscaler-ips/refs/heads/main/zscaler-ips-recommended-v6.rsc" mode=https dst-path=zscaler-ips-recommended-v6.rsc;

:log info "Remove current Zscaler IPs";
/ip firewall address-list remove [find where list="zscaler-ips-ipv4"];
/ipv6 firewall address-list remove [find where list="zscaler-ips-ipv6"];
:log info "Import newest Zscaler IPs";
/import file-name=zscaler-ips-recommended-v4.rsc;
/import file-name=zscaler-ips-recommended-v6.rsc;
```

### Sample Schedule

```
/system scheduler
add interval=1d name=zscaler-ips on-event=cloudflare-ips policy=ftp,read,write,test start-date=2025-04-23 start-time=06:45:00
```
