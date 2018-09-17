# file_crypto
Neat little program that can encrypt and decrypt files 
## Specifications: ##

* Encryption algorithm AES (Encrypting 256bit blocks)
* Key size 256bit
* MD5 (message-digest algorithm) is used to hash the key
* So far only supports files with size less than 2Gb
* Use pass phrase with more than 14 symbols for extra security
* To be able to type key with spaces put it in "Double quotation marks"

## Setup: ##
* Download/Update Python
* Install/Update required libraries (pip install -r requirements.txt)
* Put folder of script into path (Environment variables for windows)
* Add .PY extension on Pathext (Environment variables for windows)
* Encrypt by typing AES -e "filename.file" -k "key phrase" in desired path of target file
* Decrypt by typing AES -d "filename.file" -k "key phrase" in desired path of target file

