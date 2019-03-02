import argparse
import json

import urllib3
import requests
from requests.exceptions import ConnectionError, ConnectTimeout

import xmltodict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


URL = "https://{ip}/api/?key={key}&type=op&cmd=<show><system><info></info></system></show>"


def main(key, ip):
    while True:
        try:
            res = requests.get(URL.format(key=key, ip=ip),
                               timeout=5, verify=False)
        except (ConnectTimeout, ConnectionError):
            continue

        if res.status_code == 200:
            break

    print(json.dumps(xmltodict.parse(res.text), indent=4))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Check PaloALto FW status')
    parser.add_argument('--key', type=str, help='REST API Key')
    parser.add_argument('--ip', type=str, help='Management IP address')
    args = parser.parse_args()

    main(key=args.key, ip=args.ip)
