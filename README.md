# cambo

Simple camera robot

## Setup

```bash
python3.7 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install flask dotenv flask-socketio
```

## Usage

```bash
cd ~/mjpg-streamer/mjpg-streamer-experimental
mjpg_streamer -i "input_raspicam.so" -o "output_http.so" &
cd ~/Code/cambo/cambo_server
python3 cambo.py
```

Load website at [http://cammy.local:5000](http://cammy.local:5000).


