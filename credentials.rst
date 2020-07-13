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


.. _eui_login:

EUI Login
#########
Username: MUser
Password: 1234


.. _mcc_login:

MCC Login
#########
Username: MUser
Password: Tekniker2020
