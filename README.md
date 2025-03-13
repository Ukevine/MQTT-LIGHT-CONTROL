# MQTT Light Control
A web-based app to control a simulated light via MQTT.

## Files
- `index.html`: Web interface with ON/OFF buttons.
- `light_simulation.py`: Simulated IoT device that listens to MQTT messages.

## How to Run
1. Install Python and `paho-mqtt` (`pip install paho-mqtt`).
2. Run `python light_simulation.py`.
3. Open `index.html` in a browser (e.g., via `python -m http.server`).
4. Click buttons to test.

## Broker
Uses `test.mosquitto.org` (WebSocket: 8080, TCP: 1883).