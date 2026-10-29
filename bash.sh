
#!/bin/bash

read -p "Enter target host/IP: " host
ports=(22 23 25 53 80 110 443 3389)

echo "Scanning host..."
echo "----------------------"

for port in "${ports[@]}"; do
    timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "Port $port : OPEN"
    else
        echo "Port $port : CLOSED"
    fi
done