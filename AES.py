# Author: Haroldas Orestas
# Project: File encryption / decryption program

from crypto_AES_byte import AESCipher_bytes
import argparse
import os

# Method that encrypts the file
# input: Filename - String of a file name (with an extension)
# password: String of a key that is used to encrypt

def encrypt(filename, password):
    data_reader = open(filename, 'rb')
    cypher = AESCipher_bytes(password).encrypt(data_reader.read())
    data_reader.close()
    data_writer = open(filename, 'wb')
    data_writer.write(cypher)
    data_writer.close()

# Method that decrypts the file
# input: Filename - String of a file name (with an extension)
# password: String of a key that is used to decrypt

def decrypt(filename, password):
    data_reader = open(filename, 'rb')
    plain = AESCipher_bytes(password).decrypt(data_reader.read())
    data_reader.close()
    data_writer = open(filename, 'wb')
    data_writer.write(plain)
    data_writer.close()


# Below is program logic

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--efilename", help="Encrypt")
parser.add_argument("-d", "--dfilename", help="Decrypt")
parser.add_argument("-k", "--password", help="Password")

args = parser.parse_args()

def help():
    print('Commands: \n'
          '-e <file name> for encryption\n'
          '-d <file name> for decryption\n'
          '-k <key> to input the key (Mandatory)')

if(args.password != None):
    if(args.efilename != None):
        print('Starting encrypting...')
        encrypt(os.getcwd()+'\\'+args.efilename,args.password)
        print('Done...')
    else:
        if(args.dfilename != None):
            print('Starting decrypting...')
            decrypt(os.getcwd()+'\\'+args.dfilename, args.password)
            print('Done...')
        else:
            help()
else:
    help()

