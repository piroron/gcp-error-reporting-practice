# run configuration

Set your environment variable in your shell session.

`project name` format: `projects/xxx`

## Mac or Linux

```bash
export GCP_PROJECT_NAME=[project name]
```

## Windows(PowerShell)

```powershell
$env:GCP_PROJECT_NAME=[project name]
```

# setup python library
After Python 3.9

## venv
### Mac
```bash
python3 -m venv venv --upgrade-deps
. ./venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

# run

```bash
python -m main
```
