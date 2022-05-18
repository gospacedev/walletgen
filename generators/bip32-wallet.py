from mnemonic import Mnemonic
import bip32utils
#Generate new seed phrase
mnemon = Mnemonic("english")
words = mnemon.generate(256)
mnemon.check(words)
seed = mnemon.to_seed(words)

RootKey = bip32utils.BIP32Key.fromEntropy(seed)
#Create new child key
ChildKey = RootKey.ChildKey(0).ChildKey(0)
#Create new public address
PublicAddress = ChildKey.Address()
#Create new public key
PublicKey = ChildKey.PublicKey().hex()
#Create new private key
PrivateKey = ChildKey.WalletImportFormat()

print("Generated BIP32 Wallet: ")
print("Public Address: " + PublicAddress)
print("Public Key: " + PublicKey)
print("Private Key: " + PrivateKey)
