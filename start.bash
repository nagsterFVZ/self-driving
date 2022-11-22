echo "Starting Redis Server"
sudo /etc/init.d/redis-server start
echo "Starting ingest and flask app"
pm2 start ecosystem.config.js
echo "Restarting Nginx"
sudo systemctl restart nginx
echo "Startup completed"
