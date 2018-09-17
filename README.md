# file_crypto
Neat little program that can encrypt and decrypt files 
## Specifications: ##

* Encryption algorithm AES (Encrypting 256bit blocks)
* Key size 256bit
* MD5 (message-digest algorithm) is used to hash the key
* Use passphrase with more than 14 symbols for extra security
* To be able to type key with spaces put it in "Double quotation marks"

## Setup: ##
* Download/Update Python and required libraries
* Put folder of script into path (Enviroment variables for windows)
* Add .PY extension on Pathext (Enviroment variables for windows)
* Encrypt by typing AES -e "filename.file" -k "key phrase" in desired path of target file
* Decrypt by typing AES -d "filename.file" -k "key phrase" in desired path of target file

