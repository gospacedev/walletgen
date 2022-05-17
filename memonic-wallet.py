from mnemonic import Mnemonic
import bip32utils
#Memonic wallets generated there keys from a string of words
mnemon = Mnemonic("english")
words = mnemon.generate(256)
mnemon.check(words)
seed = mnemon.to_seed(words)
#Generate root key from seedphrase
RootKey = bip32utils.BIP32Key.fromEntropy(seed)
#Create new child key
ChildKey = RootKey.ChildKey(0).ChildKey(0)
#Create new public address
PublicAddress = ChildKey.Address()
#Create new public key
PublicKey = ChildKey.PublicKey().hex()
#Create new private key
PrivateKey = ChildKey.WalletImportFormat()

print("Memonic Phrase: " + words)
print("BIP39 Seed: " + seed.hex())
print("\n")
print("Generated Wallet: ")
print("Public Address: " + PublicAddress)
print("Public Key: " + PublicKey)
print("Private Key: " + PrivateKey)