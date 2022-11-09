# Setting up Circuit Python Blinka
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
echo "Starting Redis Server"
/etc/init.d/redis-server start
echo "Starting ingest and flask app"
pm2 start ecosystem.config.js
echo "Restarting Nginx"
systemctl restart nginx
echo "Startup completed"