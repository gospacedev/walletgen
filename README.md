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

### For Coffee
[![DOGE Donate](https://img.shields.io/badge/DOGE-For%20Coffee-green)](https://dogechain.info/address/DSr9btWDuDcdSg4yXkSMYjbRMLEUqp4ijt)`DSr9btWDuDcdSg4yXkSMYjbRMLEUqp4ijt`
