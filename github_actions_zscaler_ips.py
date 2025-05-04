from datetime import datetime, UTC
import requests
import json

today = datetime.now(UTC).strftime("%c") + " UTC"

zscalerHubRequiredIpsURL = "https://config.zscaler.com/api/zscaler.net/hubs/cidr/json/required"
zscalerHubRecommendedIpsURL = "https://config.zscaler.com/api/zscaler.net/hubs/cidr/json/recommended"

zscalerRequiredJson = json.loads(requests.get(zscalerHubRequiredIpsURL).content)
zscalerRecommendedJson = json.loads(requests.get(zscalerHubRecommendedIpsURL).content)

zscalerRequiredIpv4 = []
zscalerRequiredIpv6 = []
zscalerRecommendedIpv4 = []
zscalerRecommendedIpv6 = []

def generateRsc(prefixList, fileName):
    writer = open(fileName, "w")
    writer.write("# Generated on " + today)

    listName = ""

    if "v6" in fileName:
        writer.write("\n/ipv6 firewall address-list")
        listName = "zscaler-ips-ipv6"
    else:
        writer.write("\n/ip firewall address-list")
        listName = "zscaler-ips-ipv4"
    
    for prefix in prefixList:
        writer.write("\nadd list=" + listName + " address=" + prefix)

    writer.close()

def main():

    for requiredPrefix in zscalerRequiredJson["hubPrefixes"]:
        if "." in requiredPrefix:
            zscalerRequiredIpv4.append(requiredPrefix)
        else:
            zscalerRequiredIpv6.append(requiredPrefix)

    for recommendedPrefix in zscalerRecommendedJson["hubPrefixes"]:
        if "." in recommendedPrefix:
            zscalerRecommendedIpv4.append(recommendedPrefix)
        else:
            zscalerRecommendedIpv6.append(recommendedPrefix)

    generateRsc(zscalerRequiredIpv4, "zscaler-ips-required-v4.rsc")
    generateRsc(zscalerRequiredIpv6, "zscaler-ips-required-v6.rsc")
    generateRsc(zscalerRecommendedIpv4, "zscaler-ips-recommended-v4.rsc")
    generateRsc(zscalerRecommendedIpv6, "zscaler-ips-recommended-v6.rsc")

if __name__ == "__main__":
    main()
