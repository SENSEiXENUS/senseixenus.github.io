-------------

### Hooking Android Methods with Frida

------------


- Building patched apks with apktool-:

```
apktool b revme/ -o revme1.apk
```

- You have to sign it afterwards, you knowww that.

```powershell
keytool -genkey -v -keystore debug.keystore -alias androiddebugkey -keyalg DSA -sigalg  SHA1withDSA -keysize 1024 -validity 10000
jarsigner -keystore debug.keystore -verbose -storepass "password" -sigalg SHA1withDSA -digestalg SHA1 c:\Users\HP\Downloads\revme1.apk androiddebugkey
```

------------

### Installing Keytool| Jar signer

------------

- It is installed by default in java bins `C:\Program Files\Java\jre1.8.0_141\bin\`-:
- Both available in jdks

-----------------
