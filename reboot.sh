
echo "Reboot";

logFile="../logs/catalina.out"
time1=0
if [ -f $logFile ]; then
	time1=$(stat -c %Y $logFile)

	myTest=$(./shutdown.sh 2>&1 > /dev/null)
	message="Connection refused"

	if [[ $myTest == *$message* ]]; then
		echo "Server is not running."
	else
		printf "Shut down in progress"
		while sleep 1; do 
			time2=$(stat -c %Y $logFile)
			if [ $time2 -ne $time1 ]; then
				time1=$(stat -c %Y $logFile)
				lastLineOfFile=$(tail -n 2 $logFile)
				message="Destroying ProtocolHandler \[\"ajp-nio-8009\"\]"
				if [[ $lastLineOfFile == *$message* ]]; then
					echo "\nServer stopped.\n"
					break
				fi
			else
				printf "."
			fi
		done
	fi
fi

#................................................................

eval ./startup.sh;

printf "\nStartup in progress";
while sleep 1; do 
	if [ -f $logFile ]; then
		if [ $time1 -le 0 ]; then
			time1=$(stat -c %Y $logFile)
		fi
		time2=$(stat -c %Y $logFile)
		if [ $time2 -ne $time1 ]; then	
			time1=$(stat -c %Y $logFile)
			lastLineOfFile=$(tail -n 2 $logFile)
			message="org.apache.catalina.startup.Catalina.start Server startup in" # [0-9]* ms$
			if [[ $lastLineOfFile == *$message* ]]; then
				printf "\nServer is running.\n"
				exit 1;
			else
				printf "."
			fi
		fi
	else
		echo "Wait for file to be ready."
	fi
	
done

