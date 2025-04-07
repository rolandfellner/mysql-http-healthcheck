# mySQL HTTP Healthcheck

This short code creates a http endpoint at the mySQL host that can be queried from external monitoring tools. If `Status code = 200` returns everything is fine. The endpoint will be available at **Port 8080** by default. 
`URL=http://your-host-ip:8080/health`

You need a valid SQL user that can be used for the Healthcheck query.

The python script can be deployed as Docker Container. 

```
docker build -t mysql-healthcheck .
docker run -d --name mysql-healthcheck -p 8080:8080 mysql-healthcheck
```


Example Docker Run with Custom Port:

```
docker run -d \
  -p 8080:8080 \
  -e DB_HOST=your.mysql.host \
  -e DB_PORT=3307 \
  -e DB_USER=ExampleUser \
  -e DB_PASSWORD=yourStrongPass \
  -e DB_NAME=sql_monitoring_example_db \
  --name mysql-healthcheck \
  mysql-healthcheck
```



If you would like to run the script as systemd Service just copy the file mysql-healthcheck.service to the folder: `/etc/systemd/system/mysql-healthcheck.service`

and the EnvironmentFile: `/etc/mysql-healthcheck.env`

Important: You may have to adjust the user context that run the service. You can do this within the file in the [Service] section

```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable mysql-healthcheck
sudo systemctl start mysql-healthcheck
```

