import os
from flask import Flask, render_template
from dotenv import load_dotenv 
from routes.medicos_routes import medicos_bp
from routes.turnos_routes import turnos_bp

load_dotenv()
app= Flask(__name__)

app.register_blueprint(medicos_bp)
app.register_blueprint(turnos_bp)

@app.get("/")
def index():
    return render_template("index.html")
@app.get("/docs")
def docs():
    return render_template("docs.html")

if __name__ == "__main__":
    print("API REST TURNOS")
    print("docs: http://127.0.0.1:5000/docs")

app.run(debug= True, host= "0.0.0.0", port= os.getenv("puerto", default= 5000))
