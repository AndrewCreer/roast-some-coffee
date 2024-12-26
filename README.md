# Setup

Use a venv.
```
# python3 -m venv .venv
. .venv/bin/activate
```

Start webserver 
```
FLASK_APP=flaskr/app.py FLASK_DEBUG=1 flask run --host=0.0.0.0
```

## systemctl

The Debian Linux system uses systemctl to start and stop services.

To make the webserver start on boot:

```
# Note this file moght move...
sudo systemctl enable /home/pi/roast-some-coffee/systemd/coffee-webserver.service
```

