**WARNING** This project is insecure, and needs security improvments before it's
ready for prime-time.

**UNMAINTAINED**

passcrypt
==========

Cryptographically secure password manager.

# What is it?
passcrypt has one very simple goal in mind. To be a drop dead
simple password manager that holds your passwords in a
secure encrypted file. I wrote it because I needed a way to keep
my passwords and authorization tokens secure yet public, the
only real way to do this is to encrypt them. There were some
similar looking programs, but most seemed out of date or
too large, hence this.

# Installing
The goal was to make it as self contained as possible. The only
dependency is pycrypto which can be installed with pip:

    pip install pycrypto

or easy_install

    easy_install pycrypto

# Usage
```bash
$ passcrypt --help
usage: passcrypt [-h] [-o OUTPUT] [-t {blowfish,aes,des3}] [-s]
                 {get,set,del,list,passwd,create} ...

positional arguments:
  {get,set,del,list,passwd,create}
    get                 get a password
    set                 set a password.
    del                 remove a password.
    list                list passwords
    passwd              change master password.
    create              create a new password shelf.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT, --vault OUTPUT
                        file name of the password vault
  -t {blowfish,aes,des3}, --type {blowfish,aes,des3}
                        Which encryption method to use
  -s, --silent          Don't prompt for password, only works for: get, set,
                        del and list commands. *Warning* the 'silent' version
                        will echo the password. This option is for use with
                        scripts.
```
