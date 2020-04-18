# iot-device-python
Pré-requis : Installer Python sur votre ordinateur (PC, MAC)
La dernière version en date du 18/04/2020 est la 3.8.2
https://www.python.org/downloads/

Pré-requis : Installer l'extension pip
Normallement cette extension est installée avec Python. Si cela n'est pas le cas : https://pip.pypa.io/en/latest/installing/

Pour en savoir plus sur les installations de Python et pip :
https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

Vérifier que Python et pip sont correctement installés en lancant une invite de commandes.
Taper sous l'invite de commande de votre machine les commandes : python -V et pip -V (versions 3.8.2 et 20.0.2)

Normallement python s'est installé sous le répertoire c:\Python38 (sur PC Windows 10) et la variable PATH a été mise à jour (sous Windows)


Sous l'invite de commande, faites les mises à jour suivantes et installer la librairie wiotp-sdk qui permet d'accéder depuis python à la plate-forme Watson IoT :

pip install --upgrade pip 
pip install wiotp-sdk 
pip install --upgrade wiotp-sdk 

Depuis le GitHub, télécharger le code source de l'exemple (ZIP) sur votre machine dans un répertoire de votre choix, dezipper le contenu et copier le répertoire 'iot-device-python-master' sous c:\python38\

Vous obtenez :
C:\Python38\iot-device-python-master

Editer le fichier C:\Python38\iot-device-python-master\app_device\config_dev_copy.py et ajouter vos données de configuration de device crée sous la plate-forme Watson IoT sur votre compte IBM Cloud.

device_configuration = {
	"org_id"           : "uz6g30",             # replace with your organization ID
	"domain"           : "internetofthings.ibmcloud.com",
	"device_type"      : "LabPythonDevice",       # replace with your device type ID
	"device_id"        : "IoTDevice1",           # replace with your device ID
	"dev_auth_token"   : "430FEYckMPx5Ovw7mr", # replace with your device token
	"qos"              : 2,
	"disconnect_after" : 20,  # (in seconds)
	"throttleInterval" : 1000 # (in milliseconds)
}

Sauver les modifications du fichier puis lancer la commande suivante pour vérifier l'envoi des messages et leur réception dans la plate-forme : python -m app_device.send_xyz

c:\Python38\iot-device-python-master>python -m app_device.send_xyz
Wait 20 s (or press Ctrl+C to disconnect)

2020-04-18 16:14:20,577   wiotp.sdk.device.client.DeviceClient  INFO    Connected successfully: d:uz6g30:MotionDevice:terminalPython
Confirmed event at 0 ms, received by WIoTP

Confirmed event at 1000 ms, received by WIoTP

Confirmed event at 2000 ms, received by WIoTP

Confirmed event at 3000 ms, received by WIoTP

Confirmed event at 4000 ms, received by WIoTP



