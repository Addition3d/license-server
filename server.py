from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///licenses.db"
db = SQLAlchemy(app)

class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(100), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/validate", methods=["POST"])
def validate_license():
    data = request.get_json()
    machine_id = data.get("machine_id")

    if not machine_id:
        return jsonify({"status": "error", "message": "No machine_id provided"}), 400

    license_entry = License.query.filter_by(machine_id=machine_id).first()
    
    if license_entry:
        return jsonify({"status": "OK"})
    else:
        return jsonify({"status": "error", "message": "Machine not authorized"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
