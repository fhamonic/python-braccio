from braccio import Braccio
import sys

arduino_port = sys.argv[1] if len(sys.argv) else "/dev/ttyACM0"
arm = Braccio(arduino_port)

arm.home()
arm.shutdown()
