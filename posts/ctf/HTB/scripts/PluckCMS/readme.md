## CVE-2023-50564 (PoC)

This repository contains a Proof of Concept for CVE-2023-50564 vulnerability in Pluck CMS version 4.7.18

## Description

CVE-2023-50564 is a vulnerability that allows unauthorized file uploads in Pluck CMS version 4.7.18. This exploit leverages a flaw in the module installation function to upload a ZIP file containing a PHP shell, thereby enabling remote command execution.

## Usage

### Prerequisites

- Python 3.x
- The `requests` and `requests_toolbelt` packages

You can install the necessary packages with the following command:

```bash
pip install requests requests_toolbelt
```

- Usage-:

