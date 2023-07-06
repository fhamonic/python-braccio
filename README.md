# python-braccio

Install prerequisites:

    pip install pyserial

Find the Arduino USB port path:

    ./list_usb_ports.sh

Assuming its location is '/dev/ttyACM0', set the appropriate permissions:

    sudo chmod a+rw /dev/ttyACM0

Upload the arduino skecth with Arduino IDE or:

    arduino-CLI upload ./arduino_skecth --port /dev/ttyACM0

Run the python script:

    python test.py /dev/ttyACM0