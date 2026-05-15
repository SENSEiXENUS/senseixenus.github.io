------------

### Solving Frida Challenges

------------

- [Labs](http://github.com/DERE-ad2001/Frida-Labs/)

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

------------
