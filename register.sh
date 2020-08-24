_SSID=$(iwgetid -r)
_IP=$(hostname -I)
sudo rm -rf setupVars.conf
{
	echo 'PIHOLE_INTERFACE=wlan0'
	echo -n 'IPV4_ADDRESS='
	echo -n $_IP
	echo '/24'
	echo 'IPV6_ADDRESS='
	echo 'PIHOLE_DNS_1=1.1.1.1'
	echo 'PIHOLE_DNS_2=1.0.0.1'
	echo 'QUERY_LOGGING=true'
	echo 'INSTALL_WEB_SERVER=true'
	echo 'INSTALL_WEB_INTERFACE=true'
	echo 'LIGHTTPD_ENABLED=true'
	echo 'WEBPASSWORD=a3f53f1b59ca784bd8b38ac4f80b1f0c1fcc5a262c63b0edeaec66cd2601bd11'
	echo 'BLOCKING_ENABLED=false'
} >> setupVars.conf
sudo cp setupVars.conf /etc/pihole/setupVars.conf

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
	#curl -d "opr=pwdLogin&userName=*******&pwd=*******.-+&rememberPwd=1" http://1.1.1.3/ac_portal/login.php
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
#	sudo cp /etc/pihole/setupVars.conf-home /etc/pihole/setupVars.conf
	pihole enable
	printf "My wifi ssid is %s\n" "$_SSID"
fi

sleep 1

sudo python3 /home/bot/core/Autostart.py

sudo python3 /home/bot/core/detect-lcd.py
