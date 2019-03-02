# check-fw_state


## Usage :
```
usage: check-fw_state.py [-h] [--key KEY] [--ip IP]

Check PaloALto FW status

optional arguments:
  -h, --help  show this help message and exit
  --key KEY   REST API Key
  --ip IP     Management IP address
```


## Sample :
```
check-fw_state.py --key <API-KEY> --ip <IP>
{  
    "response": {
        "@status": "success",
        "result": {
            "system": {
                "hostname": "PA-AWS",
                "ip-address": "10.0.0.245",
                "netmask": "255.255.255.0",
                "default-gateway": "10.0.0.1",
                "is-dhcp": "yes",
                "ipv6-address": "unknown",
                "ipv6-link-local-address": "fe80::77:d9ff:fe4b:58/64",
                "ipv6-default-gateway": null,
                "mac-address": "02:77:d9:4b:00:58",
                "time": "Sat Mar  2 14:01:42 2019",
                "uptime": "0 days, 0:06:54",
                "devicename": "PA-AWS",
                "family": "vm",
                "model": "PA-VM",
                "serial": "4AF582D9B409254",
                "vm-uuid": "EC2A552F-4D42-C5F7-FA1C-7747662496D5",
                "vm-cpuid": "AWSMP:006bf9210f4af19a2:6kxdw3bbmdeda3o6i1ggqt4km:eu-central-1",
                "vm-license": "VM-300",
                "vm-mode": "Amazon AWS",
                "sw-version": "8.0.9",
                "global-protect-client-package-version": "0.0.0",
                "app-version": "769-4439",
                "app-release-date": "unknown",
                "av-version": "0",
                "av-release-date": "unknown",
                "threat-version": "0",
                "threat-release-date": "unknown",
                "wf-private-version": "0",
                "wf-private-release-date": "unknown",
                "url-db": "paloaltonetworks",
                "wildfire-version": "0",
                "wildfire-release-date": "unknown",
                "url-filtering-version": "0000.00.00.000",
                "global-protect-datafile-version": "unknown",
                "global-protect-datafile-release-date": "unknown",
                "global-protect-clientless-vpn-version": "0",
                "global-protect-clientless-vpn-release-date": "unknown",
                "logdb-version": "8.0.16",
                "platform-family": "vm",
                "vpn-disable-mode": "off",
                "multi-vsys": "off",
                "operational-mode": "normal"
            }
        }
    }
}
```
