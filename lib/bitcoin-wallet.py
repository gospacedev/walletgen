from bitcoin import *


def main():
    # Generate new private key
    PrivateKey = random_key()
    # Generate new public key from private key
    PublicKey = privtopub(PrivateKey)
    # Create new address from public key
    addr = pubtoaddr(PublicKey)

    print("My Public Address: " + addr)
    print("My Private Address: " + PrivateKey)


if __name__ == "__main__":
    main()
