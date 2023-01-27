import argparse
from urllib import response # for command line arguments
import requests # for http requests
import json # for json parsing

def abi_fetch(contract_address, api_key):
    ABI_ENDPOINT = f'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}'
    # ABI_ENDPOINT = f'https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}'
    response = requests.get(ABI_ENDPOINT)
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps(abi_json, indent=4, sort_keys=True)

    with open("abi.json", 'w') as file1:
        file1.write(result)
        
    return result

def main():
    contract_address = "0xe17827609Ac34443B3987661f4e037642F6BD9bA"
    api_key = "8R4URFAH5FWXDAQTDWJTRCI58KER3ZX2ZI"
    abi_fetch(contract_address, api_key)

if __name__ == "__main__":
    main()