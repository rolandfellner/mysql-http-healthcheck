
# mySQL HTTP Healthcheck

This short code creates a http endpoint at the mySQL host that can be queried from external monitoring tools. If Status code = 200 returns everything is fine. The endpoint will be available at Port 8080 by default. 
URL=http://your-host-ip:8080/health

You need a valid SQL user that can be used for the Healthcheck query.

The python script can be deployed as Docker Container:

If you would like to run the script as systemd Service just copy the file mysql-healthcheck.service to the folder: /etc/systemd/system/mysql-healthcheck.service

Important: You may have to adjust the user context that run the service. You can do this within the file in the [Service] section