# repo
Aptitude repository

## Usage

```bash
sudo apt-get update
sudo apt-get install -y curl gpg
curl -fsSL http://repo.andrew-stclair.com/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/andrew-stclair-keyring.gpg
sudo tee /etc/apt/sources.list.d/andrew-stclair.sources <<EOF
Types: deb
URIs: http://repo.andrew-stclair.com/
Suites: bookworm
Components: main
Signed-By: /usr/share/keyrings/andrew-stclair-keyring.gpg
EOF
```