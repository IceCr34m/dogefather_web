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
sudo certbot certonly --nginx
# Pinging Goole

Pinging Google via manage.py¶
django-admin ping_google [sitemap_url]¶
Once the sitemaps application is added to your project, you may also ping Google using the ping_google management command:

python manage.py ping_google [/sitemap.xml]
--sitemap-uses-http¶
Use this option if your sitemap uses http rather than https.
