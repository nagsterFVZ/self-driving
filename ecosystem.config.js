module.exports = {
  apps : [{
    name   : "ingest",
    script : "./backend/ingest.py"
  },
  {
    name   : "flask-api",
    script : "./backend/app.py"
  }]
}
