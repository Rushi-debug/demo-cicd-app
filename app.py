from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
      version = os.environ.get("APP_VERSION", "v0.0.0")
      return f"Hello from the CI/CD demo! Version: {version}\n"

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)
  
