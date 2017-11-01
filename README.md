# liferay

## stagingScript.py
Download (Recommended from liferay folder):
```
curl -o stagingScript.py https://raw.githubusercontent.com/znojProfiq/liferay/master/stagingScript.py
```

Startup:
```
python stagingScript.py
```

Output example:
```
############################
Liferay Staging setup script
############################
Set full path (not relative) to liferay portal
or leave blank (enter) if script is in root of portal folder:
Path to liferay folder is: /home/profiq/liferay-ce-portal-7.0-ga4

Using custom MySQL? (y/Enter - n):
MySQL db configuration
mySQL name (blank for "root")
mySQL password (blank for "MyNewPass4!")
### MySQL credentials ###
name: root, pass: MyNewPass4!

Set IP to allow (whole address, or just 3 last numbers for 192.168.88.XXX): 140
IP TO ALLOW: 192.168.88.140

Write data to portal-ext.properties (replace if exists)? (y/Enter - n):
tunneling.servlet.shared.secret (blank for "6162636465666768696a6b6c6d6e6f70"):
tunneling.servlet.shared.secret.hex (blank for "true") or write "false":
mySQL connection set up in /home/profiq/liferay-ce-portal-7.0-ga4/portal-ext.properties
file /home/profiq/liferay-ce-portal-7.0-ga4/portal-ext.properties was created or modified
Update TunnelAuthVerfierConfiguration automatically? (y/Enter - n):
file /home/profiq/liferay-ce-portal-7.0-ga4/osgi/configs/com.liferay.portal.security.auth.verifier.tunnel.module.configuration.TunnelAuthVerifierConfiguration-default.cfg was created or modified
Skip setup wizard in web and create config file from here? (y/Enter - n):
Email address (blank for "test@liferay.com"):
Name (blank for "Test Test"):
/home/profiq/liferay-ce-portal-7.0-ga4/portal-setup-wizard.properties created or updated

Show commands to Drop db? (y/Enter - n):
####################################################################################
DO IT YOURSELF in cmd
####################################################################################
mysql -u root -p
MyNewPass4!

DROP DATABASE lportal;
CREATE DATABASE lportal CHARACTER SET utf8 COLLATE utf8_general_ci;

####################################################################################

Turn off firewall? (Important for RedHat / CentOs) (y/Enter - n):
turn off firewall
[sudo] password for profiq:
Redirecting to /bin/systemctl stop firewalld.service

Download reboot.sh script to folder "tomcat-8.0.32/bin/"? (y/Enter - n):
file /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32/bin/reboot.sh will be downloaded by curl
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1292  100  1292    0     0   2934      0 --:--:-- --:--:-- --:--:--  2929
extend permissions for /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32/bin/reboot.sh

Run liferay? (y/Enter - n): n
Script finished successfully
```

## reboot.sh
Has to be run from [liferay portal folder]/tomcat-8.0.32/bin/
```
./reboot.sh
```

Output example:
```
Reboot
Shut down in progress...................
Server stopped.

Using CATALINA_BASE:   /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32
Using CATALINA_HOME:   /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32
Using CATALINA_TMPDIR: /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32/bin/bootstrap.jar:/home/profiq/liferay-ce-portal-7.0-ga4/tomcat-8.0.32/bin/tomcat-juli.jar
Tomcat started.

Startup in progress......................................................
Server is running.

```