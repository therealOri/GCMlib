<h1 align="center">
	<img src="https://user-images.githubusercontent.com/45724082/207946199-691bd4b7-d3f1-4187-8e54-32c6ce23503d.png">
  <br>
    GCMlib - A minimalistic and simple encryption library. For encrypting data using AES GCM mode. 
</h1>
<p align="center">
    GCMlib allows you to encrypt and decrypt data via AES in GCM mode with a password derived key. Your encrypted data/strings can only be decrypted using the aformentioned key. You can use this for a variety of things from securing passwords, encrypting HWIDs and files. Making AES encryption a little bit easier!
</p>

<h1></h1>

<br />
<br />

# Updates
What has been updated as of | 01/17/23:

> - Functions now take "keyword arguments" and `gcm.py` will enforce the "keyword arguments".


<br />
<br />

# Installation
 > [Directly from here/this repo.]
```bash
[therealOri ~]$ pip install git+https://github.com/therealOri/GCMlib
```

or

> [From Pypi.]
```bash
[therealOri ~]$ pip install GCMlib
```
__ __

<br />
<br />

# Code Examples
> If you would like to make this look better/more presentable. Please by all means make a pull request xD. I'm not the best with making things look great.

It is important to know that all functions will take 2 values in BYTES. The data to encrypt and the key. Make sure the data passed to the functions are in that order. Data first then Key.

The making of the "key" takes in a password (that you can make using [Genter](https://github.com/therealOri/Genter)). The key then gets used to encrypt your data.

<br />

```python
import gcm


##---------Start---------##

#Encrypting
data = b'Hello World <3'
key_data = b'abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde'

eKey = gcm.keygen(key_data) #Returns bytes and will return "None" if what's provided is less than 100 characters.
save_me = base64.b64encode(eKey) #for saving eKey to decrypt later.

input(f'Save this key so you can decrypt later: {save_me}\n\nPress "enter" to contine...')
gcm.clear() #clears terminal or cmd/powershell window.

data_enc = gcm.stringE(enc_data=data, key=eKey)
gcm.clear()
print(data_enc) # Output is b64 encoded. --> eyJub25jZSI6ICJjQjhpWmc0MWhDWXBRVXdVdW53Q0pRPT0iLCAiaGVhZGVyIjogIlJXNWpjbmx3ZEdWa0lIVnphVzVuSUVkRFRXeHBZaTRnUkU4Z1RrOVVJRlJCVFZCRlVpQlhTVlJJTGlBZ2ZDQWdUV0ZrWlNCaWVTQjBhR1Z5WldGc1QzSnBJQ0I4SUNCaUoxeDRNVE5jZUdKaFhIaGpaVng0TVdWY2VHRTRYSGhsT1VOY2VHRmxKdz09IiwgImNpcGhlcnRleHQiOiAiZ2FDSjY4N2FGVjNMMEIyb01Ecz0iLCAidGFnIjogIkJBUjlmVzkzaWFESnUwckpSU2o3VEE9PSJ9



#Decrypting
data = 'eyJub25jZSI6ICJjQjhpWmc0MWhDWXBRVXdVdW53Q0pRPT0iLCAiaGVhZGVyIjogIlJXNWpjbmx3ZEdWa0lIVnphVzVuSUVkRFRXeHBZaTRnUkU4Z1RrOVVJRlJCVFZCRlVpQlhTVlJJTGlBZ2ZDQWdUV0ZrWlNCaWVTQjBhR1Z5WldGc1QzSnBJQ0I4SUNCaUoxeDRNVE5jZUdKaFhIaGpaVng0TVdWY2VHRTRYSGhsT1VOY2VHRmxKdz09IiwgImNpcGhlcnRleHQiOiAiZ2FDSjY4N2FGVjNMMEIyb01Ecz0iLCAidGFnIjogIkJBUjlmVzkzaWFESnUwckpSU2o3VEE9PSJ9'
b64_enc_key = input("base64 encoded bytes/key made with keygen(): ")
dKey = base64.b64decode(b64_enc_key)

str_dcr = gcm.stringD(dcr_data=data, key=dKey)
gcm.clear()
print(str_dcr.decode('utf-8') # Output is "Hello World <3"

##---------End---------##
```

<br />

__ __

<br />

# Disclaimer
I am not liable or responsible for any data loss or destruction of any kind when using GCMlib. If you lose data and do not have backups then that is solely on you.
__ __



<br />

# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

