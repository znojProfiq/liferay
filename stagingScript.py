# ########### #
# Jiri Znoj   #
# 1. 11. 2017 #
# ########### #

# declaration
import os

sqlName = "root"
sqlPass = "MyNewPass4!"

# execution
print "############################"
print "Liferay Staging setup script"
print "############################"
print "Set full path (not relative) to liferay portal"
liferayPath = raw_input("or leave blank (enter) if script is in root of portal folder: ")
if len(liferayPath) == 0:
    liferayPath = os.getcwd()
print "Path to liferay folder is: " + liferayPath + "\n"

isMySQL = raw_input("Using custom MySQL? (y/Enter - n): ")
if isMySQL != "n":
    print("MySQL db configuration")
    sqlName = raw_input("mySQL name (blank for \"root\")")
    if len(sqlName) == 0:
        sqlName = "root"
    sqlPass = raw_input("mySQL password (blank for \"MyNewPass4!\")")
    if len(sqlPass) == 0:
        sqlPass = "MyNewPass4!"

    print "### MySQL credentials ###"
    print "name: " + sqlName + ", pass: " + sqlPass + "\n"
else:
    print("No MySQL\n")

# the additional IP addresses used in the Hosts allowed field.
ipToAllow = raw_input("Set IP to allow (whole address, or just 3 last numbers for 192.168.88.XXX): ")
if len(ipToAllow) <= 3:
    ipToAllow = "192.168.88." + ipToAllow
print "IP TO ALLOW: " + ipToAllow + "\n"

createFile = raw_input("Write data to portal-ext.properties (replace if exists)? (y/Enter - n): ")
if createFile != "n":
    filePortalName = "portal-ext.properties"
    filePortalName = os.path.join(liferayPath, filePortalName)
    # open file stream
    filePortal = open(filePortalName, "w+")

    secret = raw_input("tunneling.servlet.shared.secret (blank for \"6162636465666768696a6b6c6d6e6f70\"): ")
    if len(secret) == 0:
        secret = "6162636465666768696a6b6c6d6e6f70"
    filePortal.write("tunneling.servlet.shared.secret=" + secret + "\n")
    hex = raw_input("tunneling.servlet.shared.secret.hex (blank for \"true\") or write \"false\": ")
    if len(hex) != "false":
        hex = "true"
    filePortal.write("tunneling.servlet.shared.secret.hex=" + hex + "\n")
    filePortal.write("tunnel.servlet.hosts.allowed=127.0.0.1,SERVER_IP," + ipToAllow + "\n")
    filePortal.write("axis.servlet.hosts.allowed=127.0.0.1,SERVER_IP," + ipToAllow + "\n")
    filePortal.write("auth.verifier.TunnelingServletAuthVerifier.hosts.allowed=" + ipToAllow + "\n")

    # mysql connection
    if isMySQL != "n":
        filePortal.write("jdbc.default.driverClassName=com.mysql.jdbc.Driver\n")
        filePortal.write(
            "jdbc.default.url=jdbc:mysql://localhost/lportal?useUnicode=true&characterEncoding=UTF-8&useFastDateParsing=false\n")
        filePortal.write("jdbc.default.username=" + sqlName + "\n")
        filePortal.write("jdbc.default.password=" + sqlPass + "\n")
        print "mySQL connection set up in " + filePortalName

    print "file " + filePortalName + " was created or modified"
    # Close opened file
    filePortal.close()

    setAuth = raw_input("Update TunnelAuthVerfierConfiguration automatically? (y/Enter - n): ")
    if setAuth != "n":
        fileAuthName = "com.liferay.portal.security.auth.verifier.tunnel.module.configuration.TunnelAuthVerifierConfiguration-default.cfg"
        fileAuthNamePom = os.path.join(liferayPath, 'osgi')
        fileAuthNamePom = os.path.join(fileAuthNamePom, 'configs')
        fileAuthName = os.path.join(fileAuthNamePom, fileAuthName)

        # open file stream
        fileAuth = open(fileAuthName, "w+")
        fileAuth.write("enabled=true\n")
        fileAuth.write("hostsAllowed=127.0.0.1,SERVER_IP," + ipToAllow + "\n")
        fileAuth.write("serviceAccessPolicyName=SYSTEM_USER_PASSWORD\n")
        fileAuth.write("urlsIncludes=/api/liferay/do\n")

        print "file " + fileAuthName + " was created or modified"
        # Close opened file
        fileAuth.close()
    else:
        print "####################################################################################"
        print "DO IT YOURSELF in portlet"
        print "####################################################################################"
        print "navigate to the"
        print "Control Panel > Configuration > System Settings > Foundation > Tunnel Auth Verifier."
        print "Click /api/liferay/do and insert " + ipToAllow
        print "Then select Update."
        print "RESTART"
        print "####################################################################################\n"

    # Close opened file
    filePortal.close()

    setSetupWizard = raw_input("Skip setup wizard in web and create config file from here? (y/Enter - n): ")
    if setSetupWizard != "n":
        fileSetupWizardName = "portal-setup-wizard.properties"
        fileSetupWizardName = os.path.join(liferayPath, fileSetupWizardName)

        # open file stream
        fileSetupWizard = open(fileSetupWizardName, "w+")

        email = raw_input("Email address (blank for \"test@liferay.com\"): ")
        if len(email) == 0:
            email = "test@liferay.com"
        fileSetupWizard.write("admin.email.from.address=" + email + "\n")
        name = raw_input("Name (blank for \"Test Test\"): ")
        if len(name) == 0:
            name = "Test Test"
        fileSetupWizard.write("admin.email.from.name=" + name + "\n")
        fileSetupWizard.write("liferay.home=" + liferayPath + "\n")
        fileSetupWizard.write("setup.wizard.add.sample.data=on\n")
        fileSetupWizard.write("setup.wizard.enabled=false\n")

        # Close opened file
        fileSetupWizard.close()
        print fileSetupWizardName + " created or updated\n"

dropDb = raw_input("Show commands to Drop db? (y/Enter - n): ")
if dropDb != "n":
    print "####################################################################################"
    print "DO IT YOURSELF in cmd"
    print "####################################################################################"
    print "mysql -u " + sqlName + " -p"
    print sqlPass
    print ""
    print "DROP DATABASE lportal;"
    print "CREATE DATABASE lportal CHARACTER SET utf8 COLLATE utf8_general_ci;"
    print ""
    print "####################################################################################\n"

turnOffFirewall = raw_input("Turn off firewall? (Important for RedHat / CentOs) (y/Enter - n): ")
if turnOffFirewall != "n":
    print "turn off firewall"
    os.system("sudo service firewalld stop")
    print ""

downloadRebootScript = raw_input("Download reboot.sh script to folder \"tomcat-8.0.32/bin/\"? (y/Enter - n): ")
if downloadRebootScript != "n":
    tomcatBinPath = os.path.join(liferayPath, "tomcat-8.0.32")
    tomcatBinPath = os.path.join(tomcatBinPath, "bin")
    tomcatBinPath = os.path.join(tomcatBinPath, "reboot.sh")
    print "file " + tomcatBinPath + " will be downloaded by curl"
    os.system("curl -o " + tomcatBinPath + " https://raw.githubusercontent.com/znojProfiq/liferay/master/reboot.sh")
    print "extend permissions for " + tomcatBinPath
    os.system("chmod +777 " + tomcatBinPath)
    print ""

run = raw_input("Run liferay? (y/Enter - n): ")
if run != "n":
    run = raw_input("Without log? (y/Enter - n) n == with a full log: ")
    if run != "n":
        os.system("tomcat-8.0.32/bin/startup.sh")
    else:
        os.system("tomcat-8.0.32/bin/catalina.sh run")

print "Script finished successfully"
