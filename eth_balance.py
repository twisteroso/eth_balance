import requests

def get_eth_balance(address: str) -> float:
    url = f"https://api.ethplorer.io/getAddressInfo/{address}?apiKey=freekey"
    data = requests.get(url).json()
    return data.get("ETH", {}).get("balance", 0)

if __name__ == "__main__":
    addr = input("ETH address: ").strip()
    print(f"Balance: {get_eth_balance(addr):.4f} ETH")
