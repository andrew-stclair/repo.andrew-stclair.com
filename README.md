# repo
Aptitude repository

## Usage

```bash
wget http://repo.andrew-stclair.com/gpg.key -O /usr/share/keyrings/andrew-stclair-keyring.gpg
sudo tee -a /etc/apt/sources.list.d/andrew-stclair.sources <<EOF
Types: deb
URIs: http://repo.andrew-stclair.com/
Suites: bookworm
Components: main
Signed-By: /usr/share/keyrings/andrew-stclair-keyring.gpg
EOF
```