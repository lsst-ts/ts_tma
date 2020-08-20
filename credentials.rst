***********
Credentials
***********

List of credentials which are required to access various TMA software repositorys and logins.


.. _pdm_server:

Accessing La Serena PDM Server
##############################
	
	1. Obtain credentials to the La Serena PDM Server by asking a memeber of the La Serena IT team.

	2. Download OpenVPN and enter the IP address `139.229.195.251`. Connect to this IP.

	.. image:: _static/images/openvpn1.png

	3. Enter the credential given to you by IT

	.. image:: _static/images/openvpn2.png

	4. Connect to the server using the mac finder

	.. image:: _static/images/openvpn3.png

	5. Now in your finder window you will have access to the TSS-Share folder.


.. _nexus_repo:

Accessing Nexus Repo
####################

	1. Acquire credentials to the nexus server by asking IT for credentials. You can verify your credentials by visiting https://repo-nexus.lsst.org/nexus/#browse/welcome and logging in.

	2. In a terminal window do `docker login ts-dockerhub.lsst.org`, use the credenitals from step #1, not your regular docker credentials which may differ.

	3. You should now be able to pull any of the repositories from the `ts-dockerhub` folder within https://repo-nexus.lsst.org/nexus/#browse/welcome. The one that this documentation is concerned with is `tma_software`

	.. image:: _static/images/nexus3server.png


.. _hmi-login:

HMI Login
#########
Username: MUser
Password: 1234


.. _mcc-login:

MCC Login
#########
Username: MUser
Password: Tekniker2020


.. _finding-your-ip-subnet:

Finding your IP & Subnet
########################
Here are methods for finding your subnet depending on the OS your are on. The Subnet is the first 3 sets of numbers of your IP. For example if your computer Y has an IP address of `172.17.0.1` then the subnet that this IP address is in, is `172.17.0`. Loosely speaking, if you want to have another machine X pingable by your computer Y then machine X would need to be in the same subnet. In other words machine X would need to have an IP address of `172.17.0.*`, where the astrisk can be anything between 0-255 AND is not already taken. In this case computer Y already occupies IP address `172.17.0.1` and so a safe IP we can assign machine X could be `172.17.0.20`. For more information consult an IT proffesional as this information is likely to not be perfect and some details ommited.

MacOSX
******

1. Open System Preferences -> Network
2. For each network interface that you are using, select it in the list on the left to view the network address. On my computer Ethernet is 10.0.1.9 and Wi-Fi is 10.0.1.24
3. Another option is to run the ifconfig command in Terminal, but there are a lot of them, so it can be confusing. en0 is probably wired and en1 is probably wifi.

CentOS7
*******
[TODO]

Windows10
*********
[TODO]

.. _changing-your-ip-windows10:

Manually setting an IP address
##############################

Manually setting the IP address of a machine is common practice when quickly setting up a network of computers together. When you manually set an IP address of a machine with the intention of enabling it to talk to another machine you need to be sure of two things. The first is you need to be sure that the IP of the two machines are on the same subnet. The second is that no two machines on the same subnet can occupy the same IP. Here are a few steps to help you manually configure the IP address depending on the OS of that machine.


Windows10
*********

1) Start by opening the Control Panel. Search for "Control Panel" in the bottom left corner search bar.
2) Select "Network and Internet"
3) Select "Network and Sharing Center"
4) Select "Change adapter settings"
5) Double click the adapter you wish to manually set the IP address for. Generally, the first adapter is for enternet. Any adapters after that are for connecting to other hardware. In the case of this documentation, the second adapter is the one we want to manually set the adapter for. 
6) Select "Properties", accept any dialogues boxes that ask you if you want to make changes. 
7) Double click "Internet Protocol Version 4 (TCP/IPv4)"
8) You can now set you IP address. In the case of this documentation regardless of what you are setting your IP address to the Subnet mask needs to be `255.255.255.0` and the Default gateway empty. There is also no need to make changes to the DNS settings.


Creating Host-Only adapter
##########################

Creating a host only adapter within Virtualbox is necessary when you want to have the virtual machine communicating to other machines other than the host. This is because by defauly Virtualbox creates 1 network adapter that is only used to talking to the host machine and generally the one that is used for internet. You should never change the first adapter as this could break your virtualmachine indefinitely. 



