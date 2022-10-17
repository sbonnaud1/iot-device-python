# iot-device-python

Cet exercice permet d'envoyer des données simulées (x,y,z) depuis un simple programme Python executé sur un PC ou un Mac vers la plate-forme IBM Watson Internet of Things (WIoT P). Le PC ou le MAC joue ainsi le role du device simulé. La plate-forme WIoT P collecte les données et est crée un compte IBM Cloud, à partir du catalogue de service.

Pré-requis : Installer Python sur votre ordinateur (PC, MAC)
https://www.python.org/downloads/

Pré-requis : Installer l'extension pip
Normallement cette extension est installée avec Python. Si cela n'est pas le cas : https://pip.pypa.io/en/latest/installing/

Pour en savoir plus sur les installations de Python et pip :
https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

Vérifier que Python et pip sont correctement installés en lancant une invite de commandes.
Taper sous l'invite de commande de votre machine les commandes : python -V et pip -V.

Vérifier que Python s'est installé correctement et la variable PATH mise à jour (sous Windows). Dans tous les cas lors de l'installation de Python, vous pouvez choisir un répertoire de votre choix.

Sous l'invite de commande, faites les mises à jour suivantes et installer la librairie wiotp-sdk qui permet d'accéder depuis python à la plate-forme Watson IoT :

pip install --upgrade pip

pip install wiotp-sdk 

pip install --upgrade wiotp-sdk 

Depuis le GitHub, télécharger le code source de l'exemple (ZIP) sur votre machine dans un répertoire de votre choix, dezipper le contenu et copier le répertoire 'iot-device-python-master' dans un endroit de votre choix sur votre poste de travail.

Vous obtenez par exemple :
C:\Python39\iot-device-python-master

Editer le fichier C:\Python39\iot-device-python-master\app_device\config_dev.py et ajouter vos données de configuration du device crée sous la plate-forme Watson IoT.

Il est nécessaire d'avoir crée au préalable un type de device 'LabPythonDevice' et un device 'IoTDevice1' dans une instance de la plate-forme Watson Internet of Things avant de pouvoir exécuter le programme principal.

Remplacer dans le fichier config_dev.py les informations de connection du device avec celles que vous avez récupérées lors de la création précédente du type et de l'instance du device (Exemple ci-dessous) :

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

Sauver les modifications du fichier puis lancer la commande suivante sous le répertoire c:\Python38\iot-device-python-master afin de vérifier l'envoi des messages et leur réception dans la plate-forme : python -m app_device.send_xyz

c:\Python39\iot-device-python-master>python -m app_device.send_xyz

Wait 20 s (or press Ctrl+C to disconnect)
2020-04-20 23:00:04,256   wiotp.sdk.device.client.DeviceClient  INFO    Connected successfully: d:uz6g30:LabPythonDevice:IoTDevice1
Event 'a' {'x': -2.109541844739039, 'y': 1.263037762777719, 'z': 0.6850603004111173} sent to WIoTP

Event 'o' {'g': 10, 'b': 8, 'a': 2} sent to WIoTP

Confirmed event at 0 ms, received by WIoTP

Confirmed event at 0 ms, received by WIoTP

Event 'a' {'x': 0.4729797329721448, 'y': -0.019858572463314524, 'z': -1.9682053134574264} sent to WIoTP

Event 'o' {'g': 10, 'b': 8, 'a': 2} sent to WIoTP

Confirmed event at 1000 ms, received by WIoTP

Confirmed event at 1000 ms, received by WIoTP

Event 'a' {'x': -0.709192389465099, 'y': 0.9815754943629975, 'z': 0.24810549122793277} sent to WIoTP

Event 'o' {'g': 10, 'b': 8, 'a': 2} sent to WIoTP

Confirmed event at 2000 ms, received by WIoTP

Event 'a' {'x': 1.9435167237400273, 'y': 1.1500987851196574, 'z': 0.3156225605864271} sent to WIoTP

Event 'o' {'g': 10, 'b': 8, 'a': 2} sent to WIoTP

Confirmed event at 3000 ms, received by WIoTP

Confirmed event at 3000 ms, received by WIoTP

Confirmed event at 3000 ms, received by WIoTP

Event 'a' {'x': 0.6511059401626016, 'y': 1.7393710549308494, 'z': 0.9541822325687821} sent to WIoTP

Event 'o' {'g': 10, 'b': 8, 'a': 2} sent to WIoTP

Confirmed event at 4000 ms, received by WIoTP

Confirmed event at 4000 ms, received by WIoTP


