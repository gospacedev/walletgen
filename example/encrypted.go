package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/gocrazygh/cipher"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Enter text: ")
	scanner.Scan()
	text := scanner.Text()

	fmt.Println("Enter password:")
	scanner.Scan()
	password := scanner.Text()

	ciphertext := cipher.Encrypt([]byte(text), password)
	fmt.Printf("Encrypted: %x\n", ciphertext)
	plaintext := cipher.Decrypt(ciphertext, password)
	fmt.Printf("Decrypted: %s\n", plaintext)
}
