module.exports = {
  apps : [{
    name   : "ingest",
    script : "./backend/ingest.py"
  },
  {
    name   : "flask-api",
    script : "./backend/app.py",
    args : "--host=0.0.0.0"
  }]
}
