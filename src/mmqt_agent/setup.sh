# Install Mosquitto MQTT broker
sudo apt update
sudo apt install -y mosquitto mosquitto-clients

sudo systemctl enable mosquitto
sudo systemctl start mosquitto