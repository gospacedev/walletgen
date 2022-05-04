package cipher

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"io"

	"golang.org/x/crypto/sha3"
)

func Encrypt(message []byte, passPhrase string) ([]byte, error) {
	key := Hash(passPhrase)
	return EncryptAES256(key, message)
}

func Decrypt(message []byte, passPhrase string) ([]byte, error) {
	key := Hash(passPhrase)
	return DecryptAES256(key, message)
}

func EncryptAES256(key []byte, plaintext []byte) (encmess []byte, err error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return
	}

	aesGCM, err := cipher.NewGCM(block)
	if err != nil {
		return
	}

	nonce := make([]byte, aesGCM.NonceSize())
	if _, err = io.ReadFull(rand.Reader, nonce); err != nil {
		return
	}

	ciphertext := aesGCM.Seal(nonce, nonce, plaintext, nil)
	encmess = ciphertext
	return
}

func DecryptAES256(key []byte, securemess []byte) (decodedmess []byte, err error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return
	}

	aesGCM, err := cipher.NewGCM(block)
	if err != nil {
		return
	}

	nonceSize := aesGCM.NonceSize()

	nonce, ciphertext := securemess[:nonceSize], securemess[nonceSize:]

	plaintext, err := aesGCM.Open(nil, nonce, ciphertext, nil)
	if err != nil {
		return
	}
	decodedmess = plaintext
	return
}

func Hash(s string) []byte {
	h := sha3.Sum256([]byte(s))
	return h[:]
}
