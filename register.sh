_SSID=$(iwgetid -r)
if [ "$_SSID" = "bskj-sh" ];then
	pihole disable
	sudo pkill -o -9 pihole-FTL
	sleep 1
	pihole disable
	sudo pkill -o -9 pihole-FTL
	sleep 1
	sudo cp /etc/resolv.conf_blackshark /etc/resolv.conf
	#sudo dhclient -v
	#sudo dhcpcd
	curl -d "opr=pwdLogin&userName=solo.huang&pwd=haq*963.-+&rememberPwd=1" http://1.1.1.3/ac_portal/login.php
fi

if [ "$_SSID" = "m3p" ];then
	#sudo dhclient -v
	#sudo dhcpcd
	pihole disable
	sudo pkill -o -9 pihole-FTL
	sleep 1
	pihole disable
	sudo pkill -o -9 pihole-FTL
	sleep 1
	printf "My wifi ssid is %s\n" "$_SSID"
fi

if [ "$_SSID" = "2GWifi" ];then
	sudo cp /etc/pihole/setupVars.conf-home /etc/pihole/setupVars.conf
	printf "My wifi ssid is %s\n" "$_SSID"
fi

sleep 1

sudo python3 /home/bot/core/Autostart.py

sudo python3 /home/bot/core/detect-lcd.py
