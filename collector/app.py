from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import platform
import datetime

app = Flask(__name__)
# Enable CORS so the dashboard (different port) can call this API
CORS(app)

@app.route('/status')
def status():
    """Return system metrics as JSON."""
    # Get CPU usage (wait 1 second for accurate reading)
    cpu_percent = psutil.cpu_percent(interval=1)

    # Get memory info
    memory = psutil.virtual_memory()

    # Get disk info (root partition)
    disk = psutil.disk_usage('/')

    # Get uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    # Build response
    return jsonify({
        "hostname": platform.node(),
        "platform": platform.system(),
        "uptime": str(uptime).split('.')[0],  # Remove microseconds
        "cpu": {
            "percent": cpu_percent,
            "cores": psutil.cpu_count()
        },
        "memory": {
            "total_gb": round(memory.total / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "percent": memory.percent
        },
        "disk": {
            "total_gb": round(disk.total / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "percent": disk.percent
        }
    })

@app.route('/')
def home():
    """Simple homepage."""
    return jsonify({
        "service": "Metrics Collector",
        "status": "running",
        "endpoint": "/status"
    })

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) so it's reachable from other containers
    app.run(host='0.0.0.0', port=6000, debug=False)
