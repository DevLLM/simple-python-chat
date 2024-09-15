from app import app, socketio

if __name__ == "__main__":
  socketio.run(app)

# Gunicorn et WSGI (Web Server Gateway Interface) sont tous deux des composants utilisés dans le déploiement et la diffusion d'applications Web Python, en particulier celles créées avec des frameworks Web comme Flask et Django.