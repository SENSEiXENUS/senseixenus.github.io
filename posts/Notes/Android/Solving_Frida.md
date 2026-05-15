------------

### Solving Frida Challenges

------------

- [Labs](http://github.com/DERE-ad2001/Frida-Labs/)
- Hooking Method
```js
//Hooking methods
Java.perform(function() {
    var mainActivity = Java.use('com.ad2001.frida0x1.MainActivity');
    //Textview
    mainActivity.get_random.overload().implementation = function() {
        console.log('[+] Hooked get_random');
        return 1;
    }
})
```
- Lab2(Hooking Static Method)-> Since the  function ain't getting clicked, you have to call it yourself

```java
public static void get_flag(int a) {
        if (a == 4919) {
            try {
                SecretKeySpec secretKeySpec = new SecretKeySpec("HILLBILLWILLBINN".getBytes(), "AES");
                Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
                IvParameterSpec iv = new IvParameterSpec(new byte[16]);
                cipher.init(2, secretKeySpec, iv);
                byte[] decryptedBytes = cipher.doFinal(Base64.decode("q7mBQegjhpfIAr0OgfLvH0t/D0Xi0ieG0vd+8ZVW+b4=", 0));
                String decryptedText = new String(decryptedBytes);
                t1.setText(decryptedText);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

```

- Script-:

```js
Java.perform(function() {
    var check = Java.use("com.ad2001.frida0x2.MainActivity");
    check.get_flag(4919);
})
```
- Changing the values of a variable-:

```
Java.perform(function() {
    var checker =  Java.use('com.ad2001.frida0x3.Checker');
    checker.code.value = 512;
})
```
------------
