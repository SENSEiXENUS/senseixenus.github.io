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
- [Apk file](https://github.com/IR0NBYTE/Reverse-Engineering-Practice/blob/main/revme.apk)
- Solve-: 

```js
//Running it-:  frida -U -f com.example.basic_rev -l "C:\Users\HP\Downloads\revme\hook.js"
Java.perform(function(){
    Java.scheduleOnMainThread(function() {
      console.log("[+] Starting solve script");

      var targetClass =  Java.use("com.example.basic_rev.MainActivity");
      var makeFlag = targetClass.makeFlag;
      makeFlag.implementation = function(seed) {
        console.log("[+] Make flag called with seed "+ seed);
        var result =  makeFlag.call(this,seed);
        console.log("[+] Makeflag result::" + result);
        return result;
      };
    })
})
```
- Hooking shared libraries (.so) files-:
- Checking for modules and base address-:

```js
//Format-: frida -U -n boxy -l hook.js
var libboxy = Process.getModuleByName("libboxy.so");
console.log("[+] Library base address" + libboxy.base);
//Exported functions
var exportedFunctions =  libboxy.enumerateExports();
exportedFunctions.forEach(function(exp) {
    console.log("[+] Exported functions")
    console.log("[+]" + exp.name + " at " + exp.address);
})
 //Imported functions
var importedFunctions =  libboxy.enumerateImports();
importedFunctions.forEach(function(imp) {
    console.log("[+] Imported functions")
    console.log(" [+] " + imp.module + imp.name + " at " + imp.address);
})
```
- Hook script( interceptor)


```js
Java.perform(function() {
    var target  = Java.use("com.example.boxy.MainActivity$1");
    const libboxy = Process.getModuleByName('libboxy.so', 'Java_com_example_boxy_MainActivity_checkCred');
    target.onClick.implementation = function(view) {
        console.log("[+] Onclick is called");
        Interceptor.attach(libboxy.getExportByName('read'), {
            onEnter(args) {
                console.log("[+] Java_com_example_boxy_MainActivity_checkCred Intercepted (onEnter)");
            },
            onLeave(retval) {
               retval.replace(0);
               console.log("[+] The return value is " + retval);
            }
       });
       this.onClick(view);
    }
});
```
------------

### Installing Keytool| Jar signer

------------

- It is installed by default in java bins `C:\Program Files\Java\jre1.8.0_141\bin\`-:
- Both available in jdks

-----------------
