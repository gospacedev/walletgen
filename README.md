# cipher
A way to encrypt strings in Go

Using md5 for hashing and Galois/Counter Mode for the keys

## Usage

```
go get github.com/gocrazygh/cipher
```

If you are working outside the GOPATH:
```
go mod init <module name>
```

Here's an example:
```go
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
```

## TODO
- [ ] Build decrypt example

## For Coffee
BTC: `1F5qqrV9bX8Z1eyvy6MBxyVCKnT8cc4Hpc`

ETH: `0x438dad39b6377db423b18e24267782a6aae8ea5b`

## Acknowledgement
https://www.thepolyglotdeveloper.com/2018/02/encrypt-decrypt-data-golang-application-crypto-packages/
