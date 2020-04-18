import time
import signal
import sys
import uuid
import argparse
import wiotp.sdk
from app_device.config_dev_copy import device_configuration

deviceConfig = {
	"identity": {
		"orgId": device_configuration['org_id'],
		"typeId": device_configuration['device_type'],
		"deviceId": device_configuration['device_id']
	},
	"auth": {
		"token": device_configuration['dev_auth_token']
	},
}

def interruptHandler(signal, frame):
	deviceCli.disconnect()
	sys.exit(0)

signal.signal(signal.SIGINT, interruptHandler)

try:
	deviceCli = wiotp.sdk.device.DeviceClient(deviceConfig)
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

print("Wait %s s (or press Ctrl+C to disconnect)\n" % device_configuration['disconnect_after'])

deviceCli.connect()
for x in range(0, device_configuration['disconnect_after']*1000, device_configuration['throttleInterval']):
	data = {"x": 3.99, "y": 3.98, "z": 3.97}

	def myOnPublishCallback():
		print("Confirmed event at %s ms, received by WIoTP\n" % x)

	success = deviceCli.publishEvent("a", "json", data, qos=2, onPublish=myOnPublishCallback)
	if not success:
		print("Not connected to WIoTP")

	time.sleep(device_configuration['throttleInterval']/1000)

# Disconnect the device and application from the cloud
deviceCli.disconnect()

