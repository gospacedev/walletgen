# cipher
Encrypts strings with AES256

## Usage

```
go get github.com/gocrazygh/cipher
```

If you are working outside the GOPATH:
```
go mod init <module-name>
```

Here's an example:
```go
package main

import (
	"fmt"

	"github.com/gocrazygh/cipher"
)

func main() {
	ciphertext,_ := Encrypt([]byte(" witch collapse practice feed shame open despair creek road again ice least"), "password")
	fmt.Printf("Encrypted: %x\n", ciphertext)
	plaintext,_ := Decrypt(ciphertext, "password")
	fmt.Printf("Decrypted: %s\n", plaintext)
}
```

Terminal output:
```
Encrypted: dae1969f44375407363e1431a9ae47b1cdd216a966afae1f2a86b4d4718a496236d408b085db4837c35358c465c3a4edf04b5acdf76d20433fe6680ba64f358eed7492465c7674fe38851f2935c99dc3e562b9de43bc5e24f75c0ddd1547111ac926d0dc1c3a66
Decrypted:  witch collapse practice feed shame open despair creek road again ice least
```
