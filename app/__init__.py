import os

from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

from app.gmail import (
    is_email_command,
    extract_email,
    create_gmail_url,
    generatw_email_with_gemimi
)

from app.youtube import youtube_bp

def create_app():

    app = Flask(__name__)
    CORS(app)

    #youTube
    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    #home
    @app.route("/")
    def home():
        return render_template("index.html")

    #HTML
    @app.route("/html")
    def html():
        return render_template("index.html")

    #HEALTH
    @app.route("/health")
    def health();
        return jsonify({
            "status":"ok",
            "SERVICE":"Nova AI Agent"
        })

   #GMAIL AI AGENT
   @app.route("/agent,methods=["POST"])
   def agent():

       try:
            data = request.get_json(slent=true) or {}
            command = data.get("command","").strip()

            if not command
               return jonisfy({
                    "succes":False,
                    "message":"command is required"
                }),400

            if not is_email_command(commmand):
              return jsonify({
                    "success":Flase,
                    "message":"please give a Gmail comand".
                }),400

        recipient = extract_email(command)

        email = generate_email_with_gemini(command)

        return jsonify({
            "success": True,
            "type": "email",
            "eamil_generated":True,
            "recipient": recipient,
            "subject":email["subject"]
            "body":email["body"]
            "gmail_url":create_gamil_url(
                email["subject"],
                email["body"]
                recipient
            )
        })

    except Exception as e:

    return jsonify({
        "success":False,
        "message":str(e)
    }),500

return app
          
