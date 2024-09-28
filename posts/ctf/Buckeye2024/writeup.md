--------------

### CTF: BUCKEYE2024

---------------

![image](https://github.com/user-attachments/assets/e9cf2c6e-89ac-40ec-86d6-918a03e95614)

---------------

### Challenges

- Web
  - SFSS

---------------

### WEB

---------------

### SFSS

![image](https://github.com/user-attachments/assets/937cf518-0698-403f-90c6-2a50a03a5662)

- The web app is vulnerable to path traversal which involves using the dot-dot slash characters to read a file.The route `download` contains
the sink code.
      
      @app.route('/download/<path:file_id>')
      def download(file_id):
          file_id = filter_file_id(file_id)
      
          if file_id is None:
              return {'status': 'error', 'message': 'Invalid file id'}, 400
      
          if not os.path.exists('uploads/' + file_id):
              return {'status': 'error', 'message': 'File not found'}, 404
          
          if not os.path.isfile('uploads/' + file_id):
              return {'status': 'error', 'message': 'Invalid file id'}, 400
      
          return send_file('uploads/' + file_id, download_name=f"{file_id}.{file_exts.get(file_id, 'UNK')}")

- The `send_file()` function is vulnerable to path traversal if the file value can be controlled by an attacker.The `download` route in this case
passes the `file_id` path variable into send file.We can control the path to read the flag file.

      return send_file('uploads/' + file_id, download_name=f"{file_id}.{file_exts.get(file_id, 'UNK')}")

### Exploitation

- To prevent the web app from interpreting the `../` pattern
