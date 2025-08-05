from gpiozero import DigitalInputDevice
import time
 
d0_input = DigitalInputDevice(17)
 
while True:
  if (not d0_input.value):
    print('Moisture threshold reached!!!')
  else:
    print('You need to water your plant')
    time.sleep(2)
