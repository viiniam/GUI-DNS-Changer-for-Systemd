#!/bin/bash

#sudo chown root:root
#sudo chmod 755
# Check if both arguments are provided
#if [ "$#" -ne 2 ]; then
#    echo "Usage: $0 <Primary_DNS> <Secondary_DNS>"
#    exit 1
#fi

PRIMARY_DNS=$1
SECONDARY_DNS=$2
CONF_FILE="/etc/systemd/resolved.conf"

# 1. Comment out existing DNS and FallbackDNS lines
# ^#? matches lines that might already be commented
sed -i 's/^DNS/#DNS/' $CONF_FILE
sed -i 's/^FallbackDNS/#FallbackDNS/' $CONF_FILE

# 2. Append the new DNS settings to the file
echo -e "\nDNS=$PRIMARY_DNS\nFallbackDNS=$SECONDARY_DNS" | tee -a $CONF_FILE > /dev/null

# 3. Restart systemd-resolved to apply changes
systemctl restart systemd-resolved.service