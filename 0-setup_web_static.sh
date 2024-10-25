#!/usr/bin/env bash
#setup web server for deployment

if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install -y nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<html>
<head>
</head>
<body>
	Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f //data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^\tlocation \/ {$/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

sudo service nginx restart

exit 0
