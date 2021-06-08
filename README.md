# dogefather_web
## Deployement (work still in progress)
### Install Docker
Uninstall old versions:

```
sudo apt-get remove docker docker-engine docker.io containerd runc
```
- Install using the repository:
```
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
Add Docker’s official GPG key:
```
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
for x86_64 / amd64 machines:
```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Install Docker Engine:
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Install Compose (docker-compose): 

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
test: 
```
docker-compose --version
```
If interested in running docker-compose as non root user see : https://docs.docker.com/engine/install/linux-postinstall/

### Install certbot
```
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
Get certificate for your website:
This command need to be run on the server that will host the website and it should be the server with IP delared in A record of the domain name.
```
sudo certbot certonly --standalone
```
#### Nginx ssl certificate optimization:
Go to this path:
```
/etc/letsencrypt
```
create this file: 
```
options-ssl-nginx.conf
```
Put this in it 
```
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
```
Run this command:
```
sudo openssl dhparam -out /etc/letsencrypt/ssl-dhparams.pem 2048
```
it will take some time to generate.

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

## Pinging Goole (work still in progress)

Pinging Google via manage.py¶
django-admin ping_google [sitemap_url]¶

Once the sitemaps application is added to your project, you may also ping Google using the ping_google management command:

python manage.py ping_google [/sitemap.xml]
--sitemap-uses-http¶
Use this option if your sitemap uses http rather than https.


## Testing the website locally (Finished probably)

### install python dependecies:
You're better by creating a separate python envirenement for the project first and activating it  whenever working on the project, if you're interested in the idea look here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

To install python required libraries for the project:
```
pip3 install -r requirements.txt
```
***Notice:*** Most linux distros (at least most somewhat ols ones) come with python2 and python3 installed or only python2, so in this case to invoke python2 you simply type 'python' and to run python 3 you need to type 'python3'. The same goes for pip: pip vs pip3. If you have created a virtual python envirenement for the project you won't be needing to worry about that as when you activate the envirenement the top level python version that will be working is the one of the envirenement.
***This project requires python 3.***
Before running the server locally make sure the 'choice' variable in dogefather_web/dogefather_web/config.py is set equal to 'local' (choice='local')
you run the server by simply typing:
```
python3 manage.py runserver
```
The server will be available at http://127.0.0.1:8000

If anything went wrong, the debug option is activated by default for now and you'll be able to see part of server erros retracement on the browser. Also when developing, you don't need to worry about putting the server down everytime you make a change, you can make the change (specialy for html code) on the go while server running and simply save  the file. and refresh the page and you'll be able to see your change.
### Working with Django templates

As the project is a Django project, it use Django Templates for creating and rendering webpage. Nothing difirents much from normal html code but in order to be able to make change in the project here is what you need to know:

When you see something like `'{{ name.some_other_name  }}'` this mean that this is a context variable and it will be injected by the backend once some browser is asking for that page.
To reference pages that exits on the server, you need to use this type of pattern : 
```
<a href="{% url 'home' %}">
```
'home' is the name of the page and when you type it like that, Django will know what name to put there once a page is asked for by the browser. 

For our project we have two urls and there name are 'home' and 'tesla'. You can find the definition of there name is this file: ./dogefather_web/Core/urls.py . It looks like this:

```
    path('', home_view, name="home"),
    path('tesla', tesla_view, name='tesla'),
```
Finally, static files need to be referenced using this pattern : `"{% static 'wp-content/plugins/elementor/assets/lib/font-awesome/js/v4-shims.mine1e3.js' %}"`
Explanation:

First all static files need to be put inside: `./deogefather_web/static`

If you have a file in: `./deogefather_web/static/rest/of/path/to/the/file` and you want to referencce it on a html page. You do it by tiping : `"{% static 'rest/of/path/to/the/file' %}"`

The location fo the two pages for the prorject are located in : 
```
dogefather_web/Core/templates/Core
```
