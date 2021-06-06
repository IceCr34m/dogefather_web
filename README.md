# dogefather_web

### Install Docker
Uninstall old versions:
sudo apt-get remove docker docker-engine docker.io containerd runc
Install using the repository
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
x86_64 / amd64
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
Install Compose
To run Compose as a non-root user, see Manage Docker as a non-root user. : https://docs.docker.com/engine/install/linux-postinstall/
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
test: docker-compose --version
Install certbot
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
get certificate
sudo certbot certonly --standalone
got to this path:
/etc/letsencrypt
create this file: options-ssl-nginx.conf
put this in it 
# This file contains important security parameters. If you modify this file
# manually, Certbot will be unable to automatically provide future security
# updates. Instead, Certbot will print and log an error message with a path to
# the up-to-date file that you will need to refer to when manually updating
# this file.

ssl_session_cache shared:le_nginx_SSL:10m;
ssl_session_timeout 1440m;
ssl_session_tickets off;

ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";
crezaate this file : sudo openssl dhparam -out /etc/letsencrypt/ssl-dhparams.pem 2048
will take a while : change to 1024 if you want less time

### Runing the server


Initially, open a CLI in the location of the `docker-compose.yml` file.

Commands:

- Build the docker images and run the website:
  ```
  docker-compose -f docker-compose.yml --env-file ./deployement/.env up -d --build
  ```
- Run the website without building it again:
  ```
  docker-compose -f docker-compose.yml --env-file ./deployement/.env up -d
  ```
- Continue running the website from a **stop** state:
  ```
  docker-compose -f docker-compose.yml --env-file ./deployement/.env start
  ```
- See the logs of the containers that are running:
  ```
  docker-compose -f docker-compose.yml --env-file ./deployement/.env logs
  ```
# Pinging Goole

Pinging Google via manage.py¶
django-admin ping_google [sitemap_url]¶
Once the sitemaps application is added to your project, you may also ping Google using the ping_google management command:

python manage.py ping_google [/sitemap.xml]
--sitemap-uses-http¶
Use this option if your sitemap uses http rather than https.
