from flask import Flask, request, jsonify, send_from_directory
from models import *
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from datetime import timedelta


load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError(
        "❌ DATABASE_URL is missing. Check your environment variables!")

# Use full URL from Render
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'anuragiitmadras'

app.config['JWT_SECRET_KEY'] = 'anuragiitmadras'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

db.init_app(app)
jwt = JWTManager(app)

# UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
UPLOAD_FOLDER = "/var/data/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {"zip", "pdf", "xlsx", "doc", "docx", "txt"}


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # 465  # SSL Port
SMTP_USERNAME = 'akanuragkumar75@gmail.com'  # Replace with your email
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')


def insert_dummy_data():
    users_data = [
        # {"email": "tech@kvqaindia.com",
        #  "username": "tech@kvqaindia", "password": "asdfgh"},
        # {"email": "akanuragkumar4@gmail.com",
        #  "username": "anuragkumar", "password": "qwerty"},
        {"email": "lav@kvqaindia.com",
            "username": "lav@kvqaindia", "password": "Noida#123"},
        {"email": "dinesh@kvqaindia.com",
            "username": "dinesh@kvqaindia", "password": "Noida#123"},
        {"email": "arun@kvqaindia.com",
            "username": "arun@kvqaindia", "password": "Noida#123"},
        {"email": "kanchan@kvqaindia.com",
            "username": "kanchan@kvqaindia", "password": "Noida#123"},
        {"email": "subhrata@kvqaindia.com",
            "username": "subhrata@kvqaindia", "password": "Noida#123"},
        {"email": "ritika@kvqaindia.com",
            "username": "ritika@kvqaindia", "password": "Noida#123"},
        {"email": "deepak@kvqaindia.com",
            "username": "deepak@kvqaindia", "password": "Noida#123"},
        {"email": "kumar@kvqaindia.com",
            "username": "kumar@kvqaindia", "password": "Noida#123"},
        {"email": "rameshwar@kvqaindia.com",
            "username": "rameshwar@kvqaindia", "password": "Noida#123"},
        {"email": "anand@kvqaindia.com",
            "username": "anand@kvqaindia", "password": "Noida#123"},
        {"email": "jk@kvqaindia.com",
            "username": "jk@kvqaindia", "password": "Noida#123"},
        {"email": "tr@kvqaindia.com",
            "username": "tr@kvqaindia", "password": "Noida#123"},
        {"email": "sn@kvqaindia.com",
            "username": "sn@kvqaindia", "password": "Noida#123"},
        {"email": "sudhir@kvqaindia.com",
            "username": "sudhir@kvqaindia", "password": "Noida#123"},
        {"email": "sm@kvqaindia.com",
            "username": "sm@kvqaindia", "password": "Noida#123"},
        {"email": "varun@kvqaindia.com",
            "username": "varun@kvqaindia", "password": "Noida#123"},
        {"email": "madhavendra@kvqaindia.com",
            "username": "madhavendra@kvqaindia", "password": "Noida#123"},
        {"email": "manjul@kvqaindia.com",
            "username": "manjul@kvqaindia", "password": "Noida#123"},
        {"email": "shiv@kvqaindia.com",
            "username": "shiv@kvqaindia", "password": "Noida#123"},
        {"email": "kv@kvqaindia.com",
            "username": "kv@kvqaindia", "password": "Noida#123"},
        {"email": "priti@kvqaindia.com",
            "username": "priti@kvqaindia", "password": "Noida#123"},
        {"email": "sk@kvqaindia.com",
            "username": "sk@kvqaindia", "password": "Noida#123"},
        {"email": "shikha@kvqaindia.com",
            "username": "shikha@kvqaindia", "password": "Noida#123"},
        {"email": "neha@kvqaindia.com",
            "username": "neha@kvqaindia", "password": "Noida#123"},
        {"email": "david@kvqaindia.com",
            "username": "david@kvqaindia", "password": "Noida#123"},
        {"email": "matteo@kvqaindia.com",
            "username": "matteo@kvqaindia", "password": "Noida#123"},
        {"email": "sujay@kvqaindia.com",
            "username": "sujay@kvqaindia", "password": "Noida#123"},
        {"email": "krishna@kvqaindia.com",
            "username": "krishna@kvqaindia", "password": "Noida#123"},
        {"email": "umair@kvqaindia.com",
            "username": "umair@kvqaindia", "password": "Noida#123"},
        {"email": "tariq@kvqaindia.com",
            "username": "tariq@kvqaindia", "password": "Noida#123"},
        {"email": "mubasheer@kvqaindia.com",
            "username": "mubasheer@kvqaindia", "password": "Noida#123"},
        {"email": "abhishek@kvqaindia.com",
            "username": "abhishek@kvqaindia", "password": "Noida#123"},
        {"email": "khadam@kvqaindia.com",
            "username": "khadam@kvqaindia", "password": "Noida#123"},
        {"email": "noman@kvqaindia.com",
            "username": "noman@kvqaindia", "password": "Noida#123"},
        {"email": "farooqui@kvqaindia.com",
            "username": "farooqui@kvqaindia", "password": "Noida#123"}
    ]

    # with app.app_context():
    #     for data in users_data:
    #         existing_user = User.query.filter_by(email=data['email']).first()
    #         if not existing_user:
    #             user = User(email=data['email'], username=data['username'])
    #             user.password_hash = generate_password_hash(
    #                 data['password'])
    #             db.session.add(user)

    with app.app_context():
        for data in users_data:
            existing_user = User.query.filter_by(email=data['email']).first()
            if not existing_user:
                user = User(email=data['email'], username=data['username'])
                user.set_password(data['password'])  # ✅ Use set_password()
                db.session.add(user)

        db.session.commit()

    admin_data = [
        {"email": "training@kvqaindia.com",
         "username": "Ritika", "password": "asdfgh"},
    ]

    with app.app_context():
        for data in admin_data:
            existing_admin = Admin.query.filter_by(email=data['email']).first()
            if not existing_admin:
                admin = Admin(email=data['email'], username=data['username'])
                admin.set_password(data['password'])  # ✅ Use set_password()
                db.session.add(admin)

        db.session.commit()


with app.app_context():
    db.create_all()
    insert_dummy_data()


@app.route('/')
def home():
    return "App Started!"


# @app.route('/get')
# def user_get():
#     users = User.query.all()
#     user_list = [
#         {"id": user.id, "email": user.email,
#             "username": user.username, "password": user.password_hash}
#         for user in users
#     ]
#     return jsonify(user_list), 200


@app.route('/get', methods=['GET'])
@jwt_required()
def user_get():
    # Get logged-in user's email
    current_user_email = get_jwt_identity()['email']
    users = User.query.filter_by(
        email=current_user_email).all()  # Fetch only their data
    user_list = [
        {"id": user.id, "email": user.email, "username": user.username}
        for user in users
    ]
    return jsonify(user_list), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # print("Email: ", email)
    # print("Password: ", password)

    user = User.query.filter_by(email=email).first()
    # ✅ Compare with check_password()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.email)
        return jsonify({'token': access_token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


# @app.route('/stage1', methods=['POST'])
# def submit_stage1():
#     try:
#         data = request.form  # Get form data

#         # Handle file uploads
#         stage1_plan = request.files.get("stage1Plan")
#         stage1_report = request.files.get("stage1Report")

#         # Save uploaded files to a directory
#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage1_plan.filename) if stage1_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage1_report.filename) if stage1_report else None

#         if stage1_plan:
#             stage1_plan.save(plan_filename)
#         if stage1_report:
#             stage1_report.save(report_filename)

#         # Create a new Stage1 record in the database
#         new_stage1 = Stage1(
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage1_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage1_report=report_filename,
#             comment=data.get("comment"),
#         )

#         db.session.add(new_stage1)
#         db.session.commit()

#         return jsonify({"message": "Stage 1 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route('/stage1', methods=['POST'])
# @jwt_required()
# def submit_stage1():
#     try:
#         data = request.form
#         current_user_email = get_jwt_identity()
#         user = User.query.filter_by(email=current_user_email).first()

#         if not user:
#             return jsonify({"error": "User not found"}), 404

#         # Handle file uploads
#         stage1_plan = request.files.get("stage1Plan")
#         stage1_report = request.files.get("stage1Report")

#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage1_plan.filename) if stage1_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage1_report.filename) if stage1_report else None

#         if stage1_plan:
#             stage1_plan.save(plan_filename)
#         if stage1_report:
#             stage1_report.save(report_filename)

#         # Store user_id with the stage1 record
#         new_stage1 = Stage1(
#             user_id=user.id,  # ✅ Store user ID
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage1_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage1_report=report_filename,
#             comment=data.get("comment"),
#         )

#         db.session.add(new_stage1)
#         db.session.commit()

#         return jsonify({"message": "Stage 1 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/stage1", methods=["POST"])
# @jwt_required()
# def submit_stage1():
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         if not user:
#             return jsonify({"error": "User not found"}), 404

#         data = request.form

#         # 🔑 REQUIRED
#         audit_number = data.get("audit_number")
#         organisation_name = data.get("organisation_name")

#         if not audit_number:
#             return jsonify({"error": "Audit number is required"}), 400

#         # 🔍 Check existing record
#         stage1 = Stage1.query.filter_by(
#             audit_number=audit_number,
#             user_id=user.id
#         ).first()

#         # 📁 FILE HANDLING
#         plan_file = request.files.get("stage1_plan")
#         report_file = request.files.get("stage1_report")

#         plan_filename = None
#         report_filename = None

#         if plan_file:
#             plan_filename = os.path.join(
#                 app.config["UPLOAD_FOLDER"], plan_file.filename
#             )
#             plan_file.save(plan_filename)

#         if report_file:
#             report_filename = os.path.join(
#                 app.config["UPLOAD_FOLDER"], report_file.filename
#             )
#             report_file.save(report_filename)

#         # 🔁 UPDATE
#         if stage1:
#             stage1.scope = data.get("scope")
#             stage1.mail_from = data.get("mail_from")
#             stage1.mail_to = data.get("mail_to")
#             stage1.selected_date = data.get("selected_date")
#             stage1.selected_comment_date = data.get("selected_comment_date")
#             stage1.comment = data.get("comment")

#             if plan_filename:
#                 stage1.stage1_plan = plan_filename
#             if report_filename:
#                 stage1.stage1_report = report_filename

#             message = "Stage 1 updated successfully"

#         # ➕ INSERT (first time)
#         else:
#             stage1 = Stage1(
#                 user_id=user.id,
#                 audit_number=audit_number,
#                 organisation_name=organisation_name,
#                 scope=data.get("scope"),
#                 stage1_plan=plan_filename,
#                 mail_from=data.get("mail_from"),
#                 mail_to=data.get("mail_to"),
#                 selected_date=data.get("selected_date"),
#                 selected_comment_date=data.get("selected_comment_date"),
#                 stage1_report=report_filename,
#                 comment=data.get("comment")
#             )
#             db.session.add(stage1)
#             message = "Stage 1 created successfully"

#         db.session.commit()
#         return jsonify({"message": message}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500

@app.route("/stage1", methods=["POST"])
@jwt_required()
def submit_stage1():
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.form
        audit_number = data.get("audit_number")
        organisation_name = data.get("organisation_name")

        if not audit_number:
            return jsonify({"error": "Audit number is required"}), 400

        stage1 = Stage1.query.filter_by(
            audit_number=audit_number,
            user_id=user.id
        ).first()

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        # 📁 FILES
        plan_file = request.files.get("stage1_plan")
        report_file = request.files.get("stage1_report")

        plan_filename = None
        report_filename = None

        if plan_file:
            plan_filename = secure_filename(plan_file.filename)
            plan_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], plan_filename)
            )

        if report_file:
            report_filename = secure_filename(report_file.filename)
            report_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], report_filename)
            )

        # 🔁 UPDATE
        if stage1:
            stage1.scope = data.get("scope")
            stage1.mail_from = data.get("mail_from")
            stage1.mail_to = data.get("mail_to")
            stage1.mail_to_report = data.get("mail_to_report")
            stage1.selected_date = data.get("selected_date")
            stage1.selected_comment_date = data.get("selected_comment_date")
            stage1.comment = data.get("comment")

            if plan_filename:
                stage1.stage1_plan = plan_filename
            if report_filename:
                stage1.stage1_report = report_filename

            msg = "Stage 1 updated successfully"

        # ➕ INSERT
        else:
            stage1 = Stage1(
                user_id=user.id,
                audit_number=audit_number,
                organisation_name=organisation_name,
                scope=data.get("scope"),
                stage1_plan=plan_filename,
                mail_from=data.get("mail_from"),
                mail_to=data.get("mail_to"),
                mail_to_report=data.get("mail_to_report"),
                selected_date=data.get("selected_date"),
                selected_comment_date=data.get("selected_comment_date"),
                stage1_report=report_filename,
                comment=data.get("comment")
            )
            db.session.add(stage1)
            msg = "Stage 1 created successfully"

        db.session.commit()
        return jsonify({"message": msg}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500




# @app.route('/stage2', methods=['POST'])
# def submit_stage2():
#     try:
#         data = request.form  # Get form data

#         # Handle file uploads
#         stage2_plan = request.files.get("stage2Plan")
#         stage2_report = request.files.get("stage2Report")

#         # Save uploaded files to a directory
#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage2_plan.filename) if stage2_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage2_report.filename) if stage2_report else None

#         if stage2_plan:
#             stage2_plan.save(plan_filename)
#         if stage2_report:
#             stage2_report.save(report_filename)

#         # Create a new Stage1 record in the database
#         new_stage2 = Stage2(
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage2_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage2_report=report_filename,
#             comment=data.get("comment"),
#         )

#         db.session.add(new_stage2)
#         db.session.commit()

#         return jsonify({"message": "Stage 2 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route('/stage2', methods=['POST'])
# @jwt_required()
# def submit_stage2():
#     try:
#         data = request.form
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         stage2_plan = request.files.get("stage2Plan")
#         stage2_report = request.files.get("stage2Report")

#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage2_plan.filename) if stage2_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage2_report.filename) if stage2_report else None

#         if stage2_plan:
#             stage2_plan.save(plan_filename)
#         if stage2_report:
#             stage2_report.save(report_filename)

#         new_stage2 = Stage2(
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage2_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage2_report=report_filename,
#             comment=data.get("comment"),
#             user_id=user.id  # Associate with logged-in user
#         )

#         db.session.add(new_stage2)
#         db.session.commit()

#         return jsonify({"message": "Stage 2 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/stage2", methods=["POST"])
# @jwt_required()
# def submit_stage2():
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         if not user:
#             return jsonify({"error": "User not found"}), 404

#         data = request.form

#         # 🔑 REQUIRED
#         audit_number = data.get("audit_number")
#         organisation_name = data.get("organisation_name")

#         if not audit_number:
#             return jsonify({"error": "Audit number is required"}), 400

#         # 🔍 Check existing record
#         stage2 = Stage2.query.filter_by(
#             audit_number=audit_number,
#             user_id=user.id
#         ).first()

#         # 📁 FILE HANDLING
#         plan_file = request.files.get("stage2_plan")
#         report_file = request.files.get("stage2_report")

#         plan_filename = None
#         report_filename = None

#         if plan_file:
#             plan_filename = os.path.join(
#                 app.config["UPLOAD_FOLDER"], plan_file.filename
#             )
#             plan_file.save(plan_filename)

#         if report_file:
#             report_filename = os.path.join(
#                 app.config["UPLOAD_FOLDER"], report_file.filename
#             )
#             report_file.save(report_filename)

#         # 🔁 UPDATE
#         if stage2:
#             stage2.scope = data.get("scope")
#             stage2.mail_from = data.get("mail_from")
#             stage2.mail_to = data.get("mail_to")
#             stage2.selected_date = data.get("selected_date")
#             stage2.selected_comment_date = data.get("selected_comment_date")
#             stage2.comment = data.get("comment")

#             if plan_filename:
#                 stage2.stage2_plan = plan_filename
#             if report_filename:
#                 stage2.stage2_report = report_filename

#             message = "Stage 2 updated successfully"

#         # ➕ INSERT (first time)
#         else:
#             stage2 = Stage2(
#                 user_id=user.id,
#                 audit_number=audit_number,
#                 organisation_name=organisation_name,
#                 scope=data.get("scope"),
#                 stage1_plan=plan_filename,
#                 mail_from=data.get("mail_from"),
#                 mail_to=data.get("mail_to"),
#                 selected_date=data.get("selected_date"),
#                 selected_comment_date=data.get("selected_comment_date"),
#                 stage1_report=report_filename,
#                 comment=data.get("comment")
#             )
#             db.session.add(stage2)
#             message = "Stage 2 created successfully"

#         db.session.commit()
#         return jsonify({"message": message}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500


@app.route("/stage2", methods=["POST"])
@jwt_required()
def submit_stage2():
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.form
        audit_number = data.get("audit_number")
        organisation_name = data.get("organisation_name")

        if not audit_number:
            return jsonify({"error": "Audit number is required"}), 400

        stage2 = Stage2.query.filter_by(
            audit_number=audit_number,
            user_id=user.id
        ).first()

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        # 📁 FILES
        plan_file = request.files.get("stage2_plan")
        report_file = request.files.get("stage2_report")
        additional_file = request.files.get("additional_data")

        plan_filename = None
        report_filename = None
        additional_filename = None

        if plan_file:
            plan_filename = secure_filename(plan_file.filename)
            plan_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], plan_filename)
            )

        if report_file:
            report_filename = secure_filename(report_file.filename)
            report_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], report_filename)
            )
        
        if additional_file:
            additional_filename = secure_filename(additional_file.filename)
            additional_file.save(os.path.join(app.config["UPLOAD_FOLDER"], additional_filename))

        # 🔁 UPDATE
        if stage2:
            stage2.scope = data.get("scope")
            stage2.mail_from = data.get("mail_from")
            stage2.mail_to = data.get("mail_to")
            stage2.mail_to_report = data.get("mail_to_report")
            stage2.selected_date = data.get("selected_date")
            stage2.selected_comment_date = data.get("selected_comment_date")
            stage2.comment = data.get("comment")

            if plan_filename:
                stage2.stage2_plan = plan_filename
            if report_filename:
                stage2.stage2_report = report_filename
            if additional_filename:
                stage2.additional_data = additional_filename

            msg = "Stage 2 updated successfully"

        # ➕ INSERT
        else:
            stage2 = Stage2(
                user_id=user.id,
                audit_number=audit_number,
                organisation_name=organisation_name,
                scope=data.get("scope"),
                stage2_plan=plan_filename,
                additional_data=additional_filename,
                mail_from=data.get("mail_from"),
                mail_to=data.get("mail_to"),
                mail_to_report=data.get("mail_to_report"),
                selected_date=data.get("selected_date"),
                selected_comment_date=data.get("selected_comment_date"),
                stage2_report=report_filename,
                comment=data.get("comment")
            )
            db.session.add(stage2)
            msg = "Stage 2 created successfully"

        db.session.commit()
        return jsonify({"message": msg}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# @app.route('/dashboard', methods=['POST'])
# def dashboard_data():
#     try:
#         data = request.get_json()

#         new_application = Dashboard(
#             org_name=data.get("org_name"),
#             audit_number=data.get("audit_number"),
#             auditor=data.get("auditor"),
#             decision_maker=data.get("decision_maker"),
#             status="Pending"  # Default status for new applications
#         )

#         db.session.add(new_application)
#         db.session.commit()

#         return jsonify({"message": "Application added successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/dashboard', methods=['POST'])
@jwt_required()
def dashboard_data():
    try:
        data = request.get_json()
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        new_application = Dashboard(
            org_name=data.get("org_name"),
            audit_number=data.get("audit_number"),
            auditor=data.get("auditor"),
            decision_maker=data.get("decision_maker"),
            status="Pending",
            user_id=user.id  # Associate with logged-in user
        )

        db.session.add(new_application)
        db.session.commit()

        return jsonify({"message": "Application added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route('/dashboard', methods=['GET'])
# def get_dashboard_data():
#     try:
#         applications = Dashboard.query.all()
#         data = [
#             {
#                 "id": app.id,
#                 "org_name": app.org_name,
#                 "audit_number": app.audit_number,
#                 "status": app.status,
#                 "auditor": app.auditor,
#                 "decision_maker": app.decision_maker,
#             }
#             for app in applications
#         ]
#         return jsonify(data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/dashboard', methods=['GET'])
# @jwt_required()
# def get_dashboard_data():
#     try:
#         current_user_email = get_jwt_identity()
#         print("Decoded JWT Identity:", current_user_email)  # ✅ Debugging

#         user = User.query.filter_by(email=current_user_email).first()

#         if not user:
#             return jsonify({"error": "User not found"}), 404

#         applications = Dashboard.query.filter_by(user_id=user.id).all()
#         data = [{"id": app.id, "org_name": app.org_name, "audit_number": app.audit_number, "status": app.status,
#                  "auditor": app.auditor, "decision_maker": app.decision_maker} for app in applications]

#         return jsonify(data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard_data():
    current_user_email = get_jwt_identity()  # Get logged-in user's email

    user = User.query.filter_by(email=current_user_email).first()

    # Filter applications where the user is a decision maker
    applications = Dashboard.query.filter(
        Dashboard.auditor.like(f"%({current_user_email})%")).all()

    # Convert query results to JSON
    applications_list = [
        {
            "id": app.id,
            "org_name": app.org_name,
            "audit_number": app.audit_number,
            "auditor": app.auditor,
            "decision_maker": app.decision_maker,
            "status": app.status
        }
        for app in applications
    ]

    return jsonify({"applications": applications_list}), 200


# @app.route('/dashboard/<int:id>', methods=['DELETE'])
# def delete_application(id):
#     try:
#         application = Dashboard.query.get(id)
#         if not application:
#             return jsonify({"error": "Application not found"}), 404

#         db.session.delete(application)
#         db.session.commit()
#         return jsonify({"message": "Application deleted successfully"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/dashboard/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_application(id):
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        application = Dashboard.query.filter_by(id=id, user_id=user.id).first()
        if not application:
            return jsonify({"error": "Application not found or unauthorized"}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({"message": "Application deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_zip', methods=['POST'])
@jwt_required()
# def upload_zip():
#     try:
#         # Get the current user from JWT token
#         user_email = get_jwt_identity()
#         user = Admin.query.filter_by(email=user_email).first()
#         if not user:
#             return jsonify({"error": "Unauthorized"}), 403
#         # Get JSON data (for org_name, audit_number, etc.)
#         data = request.form  # Use form instead of get_json() because files are included
#         # Check if file exists in request
#         if 'file' not in request.files:
#             return jsonify({"error": "No file part"}), 400
#         file = request.files['file']
#         # Validate file name
#         if file.filename == '':
#             return jsonify({"error": "No selected file"}), 400
#         if not allowed_file(file.filename):
#             return jsonify({"error": "Invalid file type. Only ZIP files are allowed"}), 400
#         # Secure filename and save it in the uploads folder
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(UPLOAD_FOLDER, filename)
#         file.save(file_path)
#         # filename = secure_filename(
#         #     folder_name + ".zip") if folder_name else secure_filename(file.filename)
#         # file_path = os.path.join(UPLOAD_FOLDER, filename)
#         # file.save(file_path)
#         # Check if an entry already exists for the user
#         # dashboard_entry = Dashboard.query.filter_by(user_id=user.id).first()
#         # if dashboard_entry:
#         #     # If exists, update the zip_file_name field only
#         #     dashboard_entry.zip_file_name = filename
#         # else:
#         # If no entry exists, create a new one
#         new_application = Dashboard(
#             org_name=data.get("org_name"),
#             audit_number=data.get("audit_number"),
#             auditor=data.get("auditor"),
#             decision_maker=data.get("decision_maker"),
#             status="Pending",
#             user_id=user.id,
#             zip_file_name=f"{filename}.zip"
#         )
#         db.session.add(new_application)
#         db.session.commit()
#         return jsonify({"message": "ZIP file uploaded and Dashboard updated", "file_path": file_path}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
def upload_zip():
    try:
        user_email = get_jwt_identity()
        user = Admin.query.filter_by(email=user_email).first()

        if not user:
            return jsonify({"error": "Unauthorized"}), 403

        data = request.form  # Use form to get form data
        print("Received Form Data:", data)  # Debugging log

        folder_name = data.get("folder_name")
        if not folder_name:
            print("Error: Folder name missing in request.")  # Debugging log
            return jsonify({"error": "Folder name is missing"}), 400

        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Only ZIP files are allowed"}), 400

        # filename = secure_filename(file.filename)
        # file_path = os.path.join(UPLOAD_FOLDER, filename)
        # Restore spaces before saving
        filename = file.filename.replace("_", " ")
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        new_application = Dashboard(
            org_name=data.get("org_name"),
            audit_number=data.get("audit_number"),
            auditor=data.get("auditor"),
            decision_maker=data.get("decision_maker"),
            status="Pending",
            user_id=user.id,
            zip_file_name=f"{folder_name}.zip"
        )

        db.session.add(new_application)
        db.session.commit()
        return jsonify({"message": "ZIP file uploaded and Dashboard updated", "file_path": file_path}), 201

    except Exception as e:
        print("Server Error:", str(e))  # Debugging log
        return jsonify({"error": str(e)}), 500


@app.route('/send-email', methods=['POST'])
def send_email():
    mail_to = request.form.get("mailTo")
    subject = request.form.get("subject")
    body = request.form.get("body")

    if not mail_to:
        return jsonify({"message": "Recipient email is required!"}), 400

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME  # Sender email
    msg["To"] = mail_to
    msg.set_content(body)

    # Attach uploaded files (if any)
    attachments = request.files.getlist("attachments")
    for file in attachments:
        msg.add_attachment(file.read(), maintype="application",
                           subtype="octet-stream", filename=file.filename)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Authenticate
            server.send_message(msg)

        return jsonify({"message": f"Email sent successfully to {mail_to}!"}), 200

    except Exception as e:
        return jsonify({"message": f"Failed to send email: {str(e)}"}), 500


# @app.route("/application/<string:organisation_name>", methods=["GET"])
# def get_application_details(organisation_name):
#     try:
#         stage1_data = Stage1.query.filter_by(organisation_name=organisation_name).first()
#         stage2_data = Stage2.query.filter_by(organisation_name=organisation_name).first()

#         if not stage1_data and not stage2_data:
#             return jsonify({"message": "No data found"}), 404

#         return jsonify({
#             "stage1": {
#                 "id": stage1_data.id if stage1_data else None,
#                 "scope": stage1_data.scope if stage1_data else None,
#                 "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
#                 "mail_from": stage1_data.mail_from if stage1_data else None,
#                 "mail_to": stage1_data.mail_to if stage1_data else None,
#                 "selected_date": stage1_data.selected_date if stage1_data else None,
#                 "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
#                 "stage1_report": stage1_data.stage1_report if stage1_data else None,
#                 "comment": stage1_data.comment if stage1_data else None
#             },
#             "stage2": {
#                 "id": stage2_data.id if stage2_data else None,
#                 "scope": stage2_data.scope if stage2_data else None,
#                 "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
#                 "mail_from": stage2_data.mail_from if stage2_data else None,
#                 "mail_to": stage2_data.mail_to if stage2_data else None,
#                 "selected_date": stage2_data.selected_date if stage2_data else None,
#                 "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
#                 "stage2_report": stage2_data.stage2_report if stage2_data else None,
#                 "comment": stage2_data.comment if stage2_data else None
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route("/application/<string:organisation_name>", methods=["GET"])
# @jwt_required()
# def get_application_details(organisation_name):
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         # Ensure the user can only access their own applications
#         stage1_data = Stage1.query.filter_by(
#             organisation_name=organisation_name, user_id=user.id).first()
#         stage2_data = Stage2.query.filter_by(
#             organisation_name=organisation_name, user_id=user.id).first()

#         if not stage1_data and not stage2_data:
#             return jsonify({"message": "No data found or unauthorized access"}), 404

#         return jsonify({
#             "stage1": {
#                 "id": stage1_data.id if stage1_data else None,
#                 "scope": stage1_data.scope if stage1_data else None,
#                 "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
#                 "mail_from": stage1_data.mail_from if stage1_data else None,
#                 "mail_to": stage1_data.mail_to if stage1_data else None,
#                 "selected_date": stage1_data.selected_date if stage1_data else None,
#                 "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
#                 "stage1_report": stage1_data.stage1_report if stage1_data else None,
#                 "comment": stage1_data.comment if stage1_data else None
#             },
#             "stage2": {
#                 "id": stage2_data.id if stage2_data else None,
#                 "scope": stage2_data.scope if stage2_data else None,
#                 "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
#                 "mail_from": stage2_data.mail_from if stage2_data else None,
#                 "mail_to": stage2_data.mail_to if stage2_data else None,
#                 "selected_date": stage2_data.selected_date if stage2_data else None,
#                 "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
#                 "stage2_report": stage2_data.stage2_report if stage2_data else None,
#                 "comment": stage2_data.comment if stage2_data else None
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/application/<string:organisation_name>", methods=["GET"])
# @jwt_required()
# def get_application_details(organisation_name):
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         # Fetch the stage 1 and stage 2 data
#         stage1_data = Stage1.query.filter_by(
#             organisation_name=organisation_name, user_id=user.id).first()
#         stage2_data = Stage2.query.filter_by(
#             organisation_name=organisation_name, user_id=user.id).first()

#         # Fetch the dashboard details for the zip file
#         dashboard_data = Dashboard.query.filter(
#             org_name=organisation_name, user_id=user.id).first()
#         print("Dashboard Data:", dashboard_data)

#         if not stage1_data and not stage2_data and not dashboard_data:
#             return jsonify({"message": "No data found or unauthorized access"}), 404

#         return jsonify({
#             "stage1": {
#                 "id": stage1_data.id if stage1_data else None,
#                 "scope": stage1_data.scope if stage1_data else None,
#                 "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
#                 "mail_from": stage1_data.mail_from if stage1_data else None,
#                 "mail_to": stage1_data.mail_to if stage1_data else None,
#                 "selected_date": stage1_data.selected_date if stage1_data else None,
#                 "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
#                 "stage1_report": stage1_data.stage1_report if stage1_data else None,
#                 "comment": stage1_data.comment if stage1_data else None
#             },
#             "stage2": {
#                 "id": stage2_data.id if stage2_data else None,
#                 "scope": stage2_data.scope if stage2_data else None,
#                 "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
#                 "mail_from": stage2_data.mail_from if stage2_data else None,
#                 "mail_to": stage2_data.mail_to if stage2_data else None,
#                 "selected_date": stage2_data.selected_date if stage2_data else None,
#                 "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
#                 "stage2_report": stage2_data.stage2_report if stage2_data else None,
#                 "comment": stage2_data.comment if stage2_data else None
#             },
#             "dashboard": {
#                 "zip_file_name": dashboard_data.zip_file_name if dashboard_data else None
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route("/application/<string:organisation_name>", methods=["GET"])
@jwt_required()
def get_application_details(organisation_name):
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Fetch the stage 1 and stage 2 data
        stage1_data = Stage1.query.filter_by(
            organisation_name=organisation_name, user_id=user.id).first()
        stage2_data = Stage2.query.filter_by(
            organisation_name=organisation_name, user_id=user.id).first()
        dashboard_data = Dashboard.query.filter_by(
            org_name=organisation_name, user_id=user.id).first()

        print("Fetched Data:", stage1_data,
              stage2_data, dashboard_data)  # Debugging

        if not stage1_data and not stage2_data and not dashboard_data:
            return jsonify({"message": "No data found or unauthorized access"}), 404

        response_data = {
            "stage1": {
                "id": stage1_data.id if stage1_data else None,
                "scope": stage1_data.scope if stage1_data else None,
                "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
                "mail_from": stage1_data.mail_from if stage1_data else None,
                "mail_to": stage1_data.mail_to if stage1_data else None,
                "selected_date": stage1_data.selected_date if stage1_data else None,
                "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
                "stage1_report": stage1_data.stage1_report if stage1_data else None,
                "comment": stage1_data.comment if stage1_data else None
            } if stage1_data else {},  # Avoid returning NoneType

            "stage2": {
                "id": stage2_data.id if stage2_data else None,
                "scope": stage2_data.scope if stage2_data else None,
                "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
                "mail_from": stage2_data.mail_from if stage2_data else None,
                "mail_to": stage2_data.mail_to if stage2_data else None,
                "selected_date": stage2_data.selected_date if stage2_data else None,
                "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
                "stage2_report": stage2_data.stage2_report if stage2_data else None,
                "comment": stage2_data.comment if stage2_data else None
            } if stage2_data else {},

            "dashboard": {
                "zip_file_name": dashboard_data.zip_file_name if dashboard_data else None
            } if dashboard_data else {}
        }

        return jsonify(response_data), 200

    except Exception as e:
        print("Error in get_application_details:", str(e))  # Print exact error
        return jsonify({"error": str(e)}), 500


# @app.route("/download/<path:filename>", methods=["GET"])
# def download_file(filename):
#     try:
#         return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 404


# @app.route("/download/<path:filename>", methods=["GET"])
# @jwt_required()
# def download_file(filename):
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         # Ensure only filename is checked (without "uploads/")
#         filename = filename.replace("uploads/", "")

#         # Check if file belongs to the user
#         stage1_file = Stage1.query.filter(
#             (Stage1.stage1_plan == filename) | (Stage1.stage1_report == filename),
#             Stage1.user_id == user.id
#         ).first()
#         stage2_file = Stage2.query.filter(
#             (Stage2.stage2_plan == filename) | (Stage2.stage2_report == filename),
#             Stage2.user_id == user.id
#         ).first()

#         if not stage1_file and not stage2_file:
#             return jsonify({"error": "File not found or unauthorized access"}), 403

#         upload_folder = "uploads"  # Ensure this matches your actual upload directory
#         return send_from_directory(upload_folder, filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 404


# @app.route("/download/<path:filename>", methods=["GET"])
# @jwt_required()
# def download_file(filename):
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         # Ensure correct filename format
#         filename = filename.replace("uploads/", "")

#         print(f"Requested file: {filename}")
#         print(f"Logged-in user: {user_email} (User ID: {user.id})")

#         # Debug: Check what filenames exist in the database
#         user_files_stage1 = Stage1.query.filter(
#             Stage1.user_id == user.id).all()
#         user_files_stage2 = Stage2.query.filter(
#             Stage2.user_id == user.id).all()

#         print(
#             f"User's Stage 1 Files: {[file.stage1_plan for file in user_files_stage1]}")
#         print(
#             f"User's Stage 2 Files: {[file.stage2_plan for file in user_files_stage2]}")

#         # Check if file belongs to the user
#         stage1_file = Stage1.query.filter(
#             (Stage1.stage1_plan == f"uploads/{filename}") | (
#                 Stage1.stage1_report == f"uploads/{filename}"),
#             Stage1.user_id == user.id
#         ).first()
#         stage2_file = Stage2.query.filter(
#             (Stage2.stage2_plan == f"uploads/{filename}") | (
#                 Stage2.stage2_report == f"uploads/{filename}"),
#             Stage2.user_id == user.id
#         ).first()

#         if not stage1_file and not stage2_file:
#             print("Unauthorized file access attempt.")
#             return jsonify({"error": "File not found or unauthorized access"}), 403

#         upload_folder = "uploads"
#         return send_from_directory(upload_folder, filename, as_attachment=True)

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return jsonify({"error": str(e)}), 404

@app.route("/download/<path:filename>", methods=["GET"])
@jwt_required()
def download_file(filename):
    user_email = get_jwt_identity()
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    print(f"Requested file: {filename}")

    # Check DB for the file belonging to this user
    stage1_file = Stage1.query.filter(
        ((Stage1.stage1_plan == filename) | (Stage1.stage1_report == filename)) &
        (Stage1.user_id == user.id)
    ).first()

    stage2_file = Stage2.query.filter(
        ((Stage2.stage2_plan == filename) | (Stage2.stage2_report == filename)) &
        (Stage2.user_id == user.id)
    ).first()

    if not stage1_file and not stage2_file:
        return jsonify({"error": "File not found or unauthorized access"}), 403

    upload_folder = app.config["UPLOAD_FOLDER"]
    return send_from_directory(upload_folder, filename, as_attachment=True)



@app.route('/search', methods=['GET'])
@jwt_required()
def search_dashboard():
    # Get the authenticated user's email from JWT
    user_email = get_jwt_identity()
    print(f"🔹 JWT Identity (Email): {user_email}")

    # Fetch user by email
    user = User.query.filter_by(email=user_email).first()
    if not user:
        print(f"❌ No user found with email: {user_email}")
        return jsonify({"error": "User not found"}), 400

    user_id = user.id
    print(f"✅ Retrieved User ID: {user_id}")

    # Get search parameters
    org_name = request.args.get("org_name", "").strip()
    audit_number = request.args.get("audit_number", "").strip()
    print(
        f"🔍 Search Parameters - Org: '{org_name}', Audit: '{audit_number}', User ID: {user_id}")

    # Build search query
    query = Dashboard.query.filter(Dashboard.user_id == user_id)

    if org_name:
        query = query.filter(Dashboard.org_name.ilike(f"%{org_name}%"))
        print(f"✅ Applied filter for org_name: {org_name}")

    if audit_number:
        query = query.filter(Dashboard.audit_number.ilike(f"%{audit_number}%"))
        print(f"✅ Applied filter for audit_number: {audit_number}")

    # Execute query
    results = query.all()
    print(f"✅ Query Results: {results}")

    # Format response
    applications = [
        {
            "id": app.id,
            "org_name": app.org_name,
            "audit_number": app.audit_number,
            "auditor": app.auditor,
            "decision_maker": app.decision_maker,
            "status": app.status,
        }
        for app in results
    ]

    return jsonify(applications), 200


@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Look up the admin by email
    admin = Admin.query.filter_by(email=email).first()

    # Verify admin credentials
    if admin and admin.check_password(password):
        access_token = create_access_token(identity=admin.email)
        return jsonify({'token': access_token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/admin/dashboard-data', methods=['GET'])
@jwt_required()  # Require authentication
def get_admin_dashboard_data():
    # Get all dashboard entries
    dashboard_entries = Dashboard.query.all()

    # Convert them into JSON format
    dashboard_data = [{
        "id": entry.id,
        "user_id": entry.user_id,
        "org_name": entry.org_name,
        "audit_number": entry.audit_number,
        "auditor": entry.auditor,
        "decision_maker": entry.decision_maker,
        "status": entry.status
    } for entry in dashboard_entries]

    return jsonify(dashboard_data), 200


@app.route('/admin/applications', methods=['GET'])
@jwt_required()  # Requires authentication
def get_applications():
    applications = Dashboard.query.all()
    result = [{
        "id": app.id,
        "user_id": app.user_id,
        "org_name": app.org_name,
        "audit_number": app.audit_number,
        "auditor": app.auditor,
        "decision_maker": app.decision_maker,
        "status": app.status
    } for app in applications]

    return jsonify(result), 200


@app.route('/admin/register_user', methods=['POST'])
@cross_origin()
def register_user():
    data = request.json
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not email or not username or not password:
        return jsonify({"error": "All fields are required"}), 400

    existing_user = User.query.filter(
        (User.email == email) | (User.username == username)).first()
    if existing_user:
        return jsonify({"error": "Email or Username already exists"}), 409

    new_user = User(email=email, username=username)
    new_user.set_password(password)  # Hash password before saving

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/admin/users', methods=['GET'])
@cross_origin()
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "email": user.email,
                  "username": user.username} for user in users]
    return jsonify({"users": user_list}), 200


@app.route('/admin/users/<int:user_id>', methods=['DELETE'])
@cross_origin()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200


# @app.route("/admin/application/<string:organisation_name>", methods=["GET"])
# def admin_get_application_details(organisation_name):
#     try:
#         # Fetch all applications for the given organisation_name
#         stage1_data = Stage1.query.filter_by(
#             organisation_name=organisation_name).all()
#         stage2_data = Stage2.query.filter_by(
#             organisation_name=organisation_name).all()

#         if not stage1_data and not stage2_data:
#             return jsonify({"message": f"No data found for organisation '{organisation_name}'"}), 404

#         # Format response
#         applications = []

#         # Process Stage 1 data
#         for stage1 in stage1_data:
#             applications.append({
#                 "organisation_name": stage1.organisation_name,
#                 "user_id": stage1.user_id,
#                 "stage1": {
#                     "id": stage1.id,
#                     "scope": stage1.scope,
#                     "stage1_plan": stage1.stage1_plan,
#                     "mail_from": stage1.mail_from,
#                     "mail_to": stage1.mail_to,
#                     "selected_date": stage1.selected_date,
#                     "selected_comment_date": stage1.selected_comment_date,
#                     "stage1_report": stage1.stage1_report,
#                     "comment": stage1.comment
#                 },
#                 "stage2": None  # Placeholder to be updated later
#             })

#         # Process Stage 2 data and match with Stage 1
#         for stage2 in stage2_data:
#             found = False
#             for app in applications:
#                 if app["organisation_name"] == stage2.organisation_name and app["user_id"] == stage2.user_id:
#                     app["stage2"] = {
#                         "id": stage2.id,
#                         "scope": stage2.scope,
#                         "stage2_plan": stage2.stage2_plan,
#                         "mail_from": stage2.mail_from,
#                         "mail_to": stage2.mail_to,
#                         "selected_date": stage2.selected_date,
#                         "selected_comment_date": stage2.selected_comment_date,
#                         "stage2_report": stage2.stage2_report,
#                         "comment": stage2.comment
#                     }
#                     found = True
#                     break

#             # If no Stage 1 entry was found, create a new entry with only Stage 2 data
#             if not found:
#                 applications.append({
#                     "organisation_name": stage2.organisation_name,
#                     "user_id": stage2.user_id,
#                     "stage1": {},  # No Stage 1 record for this user
#                     "stage2": {
#                         "id": stage2.id,
#                         "scope": stage2.scope,
#                         "stage2_plan": stage2.stage2_plan,
#                         "mail_from": stage2.mail_from,
#                         "mail_to": stage2.mail_to,
#                         "selected_date": stage2.selected_date,
#                         "selected_comment_date": stage2.selected_comment_date,
#                         "stage2_report": stage2.stage2_report,
#                         "comment": stage2.comment
#                     }
#                 })

#             print("applications:", applications)
#             print(type(applications))

#         return jsonify({"applications": applications}), 200

#     except Exception as e:
#         print(f"Admin error fetching applications: {str(e)}")  # Debugging log
#         return jsonify({"error": str(e)}), 500


@app.route("/admin/application/<string:organisation_name>", methods=["GET"])
def admin_get_application_details(organisation_name):
    try:
        # Fetch matching records
        stage1_data = Stage1.query.filter(
            Stage1.organisation_name.ilike(organisation_name)).all()
        stage2_data = Stage2.query.filter(
            Stage2.organisation_name.ilike(organisation_name)).all()
        dashboard_data = Dashboard.query.filter(
            Dashboard.org_name.ilike(organisation_name)).all()

        if not stage1_data and not stage2_data and not dashboard_data:
            return jsonify({"message": f"No data found for organisation '{organisation_name}'"}), 404

        applications = []

        # Process Stage 1 data
        for stage1 in stage1_data:
            applications.append({
                "organisation_name": stage1.organisation_name,
                "user_id": stage1.user_id,
                "stage1": {
                    "id": stage1.id,
                    "scope": stage1.scope,
                    "stage1_plan": stage1.stage1_plan,
                    "mail_from": stage1.mail_from,
                    "mail_to": stage1.mail_to,
                    "selected_date": stage1.selected_date,
                    "selected_comment_date": stage1.selected_comment_date,
                    "stage1_report": stage1.stage1_report,
                    "comment": stage1.comment
                },
                "stage2": None,
                "zip_file_name": None
            })

        # Process Stage 2 data
        for stage2 in stage2_data:
            found = False
            for app in applications:
                if app["organisation_name"] == stage2.organisation_name and app["user_id"] == stage2.user_id:
                    app["stage2"] = {
                        "id": stage2.id,
                        "scope": stage2.scope,
                        "stage2_plan": stage2.stage2_plan,
                        "mail_from": stage2.mail_from,
                        "mail_to": stage2.mail_to,
                        "selected_date": stage2.selected_date,
                        "selected_comment_date": stage2.selected_comment_date,
                        "stage2_report": stage2.stage2_report,
                        "comment": stage2.comment
                    }
                    found = True
                    break

            if not found:
                applications.append({
                    "organisation_name": stage2.organisation_name,
                    "user_id": stage2.user_id,
                    "stage1": None,
                    "stage2": {
                        "id": stage2.id,
                        "scope": stage2.scope,
                        "stage2_plan": stage2.stage2_plan,
                        "mail_from": stage2.mail_from,
                        "mail_to": stage2.mail_to,
                        "selected_date": stage2.selected_date,
                        "selected_comment_date": stage2.selected_comment_date,
                        "stage2_report": stage2.stage2_report,
                        "comment": stage2.comment
                    },
                    "zip_file_name": None
                })

        # Process Dashboard data and add zip file details
        for dashboard in dashboard_data:
            found = False
            for app in applications:
                if app["organisation_name"] == dashboard.org_name and app["user_id"] == dashboard.user_id:
                    # Ensure zip file is added to an existing application
                    app["zip_file_name"] = dashboard.zip_file_name
                    found = True
                    break

            if not found:
                # If no stage1/stage2 data but dashboard entry exists, create an entry
                applications.append({
                    "organisation_name": dashboard.org_name,
                    "user_id": dashboard.user_id,
                    "stage1": None,
                    "stage2": None,
                    "zip_file_name": dashboard.zip_file_name
                })

        # Debugging output
        print("Retrieved applications:", applications)

        return jsonify({"applications": applications}), 200

    except Exception as e:
        print(f"Error fetching applications: {str(e)}")
        return jsonify({"error": str(e)}), 500


# @app.route("/admin/download/<path:filename>", methods=["GET"])
# @jwt_required()
# def admin_download_file(filename):
#     try:

#         # Ensure correct filename format
#         filename = filename.replace("uploads/", "")

#         # Debug: Check what filenames exist in the database
#         # user_files_stage1 = Stage1.query.filter(
#         #     Stage1.user_id == user.id).all()
#         # user_files_stage2 = Stage2.query.filter(
#         #     Stage2.user_id == user.id).all()

#         # print(
#         #     f"User's Stage 1 Files: {[file.stage1_plan for file in user_files_stage1]}")
#         # print(
#         #     f"User's Stage 2 Files: {[file.stage2_plan for file in user_files_stage2]}")

#         # Check if file belongs to the user
#         stage1_file = Stage1.query.filter(
#             (Stage1.stage1_plan == f"uploads/{filename}") | (
#                 Stage1.stage1_report == f"uploads/{filename}"),
#         ).first()
#         stage2_file = Stage2.query.filter(
#             (Stage2.stage2_plan == f"uploads/{filename}") | (
#                 Stage2.stage2_report == f"uploads/{filename}"),
#         ).first()

#         # dashboard_file = Dashboard.query.filter(
#         #     Dashboard.zip_file_name == filename
#         # ).first()

#         if not stage1_file and not stage2_file:
#             # if not stage1_file and not stage2_file and not dashboard_file:
#             print("Unauthorized file access attempt.")
#             return jsonify({"error": "File not found or unauthorized access"}), 403

#         upload_folder = "uploads"
#         return send_from_directory(upload_folder, filename, as_attachment=True)

#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return jsonify({"error": str(e)}), 404


@app.route("/admin/download/<path:filename>", methods=["GET"])
@jwt_required()
def admin_download_file(filename):
    try:
        filename = filename.replace("uploads/", "")  # Remove "uploads/" prefix

        print(f"Requested filename: {filename}")  # Debug print

        # ✅ Print all available filenames in Dashboard
        all_files = Dashboard.query.with_entities(
            Dashboard.zip_file_name).all()
        # Debug print
        print(f"Database files: {[file[0] for file in all_files]}")

        # ✅ Check if the file exists in Dashboard
        dashboard_file = Dashboard.query.filter(
            # If stored without "uploads/"
            (Dashboard.zip_file_name == filename) |
            # If stored with "uploads/"
            (Dashboard.zip_file_name == f"uploads/{filename}")
        ).first()
        print(f"Dashboard file found: {dashboard_file}")

        # ✅ Check Stage1 and Stage2 tables
        stage1_file = Stage1.query.filter(
            (Stage1.stage1_plan == f"uploads/{filename}") |
            (Stage1.stage1_report == f"uploads/{filename}")
        ).first()
        stage2_file = Stage2.query.filter(
            (Stage2.stage2_plan == f"uploads/{filename}") |
            (Stage2.stage2_report == f"uploads/{filename}")
        ).first()

        # ❌ If the file is not found in any table, return an error
        if not dashboard_file and not stage1_file and not stage2_file:
            print(f"File '{filename}' not found in database.")
            return jsonify({"error": "File not found in database"}), 404

        # ✅ Ensure the file exists in the uploads directory
        upload_folder = "uploads"
        file_path = os.path.join(upload_folder, filename)

        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found in directory.")
            return jsonify({"error": "File not found in directory"}), 404

        print(f"File '{filename}' found! Sending file...")
        return send_from_directory(upload_folder, filename, as_attachment=True)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/admin/applications/<int:id>', methods=['DELETE'])
@jwt_required()
def admin_delete_application(id):
    try:
        application = Dashboard.query.filter_by(
            id=id).first()  # No user_id filter for admin
        if not application:
            return jsonify({"error": "Application not found"}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({"message": "Application deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin/applications/<int:id>/approve', methods=['PUT'])
@jwt_required()
def approve_application(id):
    try:
        # Fetch the application without filtering by user_id (Admin has access to all)
        application = Dashboard.query.filter_by(id=id).first()
        if not application:
            return jsonify({"error": "Application not found"}), 404

        # Update status to 'Approved'
        application.status = "Approved"
        db.session.commit()

        return jsonify({"message": "Application approved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin/applications/<int:id>/reject', methods=['PUT'])
@jwt_required()
def reject_application(id):
    try:
        # Fetch the application without filtering by user_id (Admin has access to all)
        application = Dashboard.query.filter_by(id=id).first()
        if not application:
            return jsonify({"error": "Application not found"}), 404

        # Update status to 'Approved'
        application.status = "Rejected"
        db.session.commit()

        return jsonify({"message": "Application rejected!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin/search', methods=['GET'])
@jwt_required()
def search_dashboard_admin():
    try:
        # Get search parameters
        org_name = request.args.get("org_name", "").strip()
        audit_number = request.args.get("audit_number", "").strip()

        print(
            f"🔍 Search Parameters - Org: '{org_name}', Audit: '{audit_number}'")

        # Build search query for the admin (No user ID restriction)
        query = Dashboard.query

        if org_name:
            query = query.filter(Dashboard.org_name.ilike(f"%{org_name}%"))
            print(f"✅ Applied filter for org_name: {org_name}")

        if audit_number:
            query = query.filter(
                Dashboard.audit_number.ilike(f"%{audit_number}%"))
            print(f"✅ Applied filter for audit_number: {audit_number}")

        # Execute query
        results = query.all()
        print(f"✅ Query Results: {results}")

        # Format response
        applications = [
            {
                "id": app.id,
                "org_name": app.org_name,
                "audit_number": app.audit_number,
                "auditor": app.auditor,
                "decision_maker": app.decision_maker,
                "status": app.status,
            }
            for app in results
        ]

        return jsonify(applications), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


# @app.route('/stage1-data', methods=['GET'])
# @jwt_required()
# def get_stage1_data():
#     org_name = request.args.get("org_name")

#     stage1_entry = Stage1.query.filter_by(
#         organisation_name=org_name).first()
#     if not stage1_entry:
#         return jsonify({"message": "No data found"}), 404

#     return jsonify({
#         "scope": stage1_entry.scope,
#         "mailTo": stage1_entry.mail_to,
#         "selectedDate": stage1_entry.selected_date,
#         "selectedCommentDate": stage1_entry.selected_comment_date,
#         "comment": stage1_entry.comment,
#         "mailToReport": stage1_entry.mail_to,
#     })

@app.route("/stage1-data", methods=["GET"])
@jwt_required()
def get_stage1_data():
    user_email = get_jwt_identity()
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    audit_number = request.args.get("audit_number")
    if not audit_number:
        return jsonify({"error": "Audit number required"}), 400

    stage1 = Stage1.query.filter_by(
        audit_number=audit_number,
        user_id=user.id
    ).first()

    if not stage1:
        return jsonify({}), 200

    return jsonify({
        "organisationName": stage1.organisation_name,
        "scope": stage1.scope or "",
        "mailTo": stage1.mail_to or "",
        "mailToReport": stage1.mail_to_report or "",
        "selectedDate": stage1.selected_date,              # yyyy-mm-dd
        "selectedCommentDate": stage1.selected_comment_date,
        "comment": stage1.comment or "",
        "stage1PlanFile": stage1.stage1_plan,              # filename only
        "stage1ReportFile": stage1.stage1_report
    }), 200




# @app.route('/stage2-data', methods=['GET'])
# @jwt_required()
# def get_stage2_data():
#     org_name = request.args.get("org_name")

#     stage2_entry = Stage2.query.filter_by(
#         organisation_name=org_name).first()
#     if not stage2_entry:
#         return jsonify({"message": "No data found"}), 404

#     return jsonify({
#         "scope": stage2_entry.scope,
#         "mailTo": stage2_entry.mail_to,
#         "selectedDate": stage2_entry.selected_date,
#         "selectedCommentDate": stage2_entry.selected_comment_date,
#         "comment": stage2_entry.comment,
#         "mailToReport": stage2_entry.mail_to,
#     })

@app.route("/stage2-data", methods=["GET"])
@jwt_required()
def get_stage2_data():
    user_email = get_jwt_identity()
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    audit_number = request.args.get("audit_number")
    if not audit_number:
        return jsonify({"error": "Audit number required"}), 400

    stage2 = Stage2.query.filter_by(
        audit_number=audit_number,
        user_id=user.id
    ).first()

    if not stage2:
        return jsonify({}), 200

    return jsonify({
        "organisationName": stage2.organisation_name,
        "scope": stage2.scope or "",
        "mailTo": stage2.mail_to or "",
        "mailToReport": stage2.mail_to_report or "",
        "selectedDate": stage2.selected_date,              # yyyy-mm-dd
        "selectedCommentDate": stage2.selected_comment_date,
        "comment": stage2.comment or "",
        "stage2PlanFile": stage2.stage2_plan,              # filename only
        "stage2ReportFile": stage2.stage2_report,
        "additionalDataFile": stage2.additional_data
    }), 200


@app.route("/users", methods=["GET"])
@jwt_required()  # Ensure only authenticated users can access this
def get_users_data():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username,
                  "email": user.email} for user in users]
    return jsonify(user_list), 200


@app.route('/decision-maker-applications', methods=['GET'])
@jwt_required()
def get_decision_maker_apps():
    current_user_email = get_jwt_identity()  # Get logged-in user's email

    # Filter applications where the user is a decision maker
    applications = Dashboard.query.filter(
        Dashboard.decision_maker.like(f"%({current_user_email})%")).all()

    # Convert query results to JSON
    applications_list = [
        {
            "id": app.id,
            "org_name": app.org_name,
            "audit_number": app.audit_number,
            "auditor": app.auditor,
            "decision_maker": app.decision_maker,
            "status": app.status
        }
        for app in applications
    ]

    return jsonify({"applications": applications_list}), 200


# @app.route("/decision/application/<string:organisation_name>", methods=["GET"])
# def decision_get_application_details(organisation_name):
#     try:
#         # Fetch all applications for the given organisation_name
#         stage1_data = Stage1.query.filter_by(
#             organisation_name=organisation_name).all()
#         stage2_data = Stage2.query.filter_by(
#             organisation_name=organisation_name).all()

#         if not stage1_data and not stage2_data:
#             return jsonify({"message": f"No data found for organisation '{organisation_name}'"}), 404

#         # Format response
#         applications = []

#         # Process Stage 1 data
#         for stage1 in stage1_data:
#             applications.append({
#                 "organisation_name": stage1.organisation_name,
#                 "user_id": stage1.user_id,
#                 "stage1": {
#                     "id": stage1.id,
#                     "scope": stage1.scope,
#                     "stage1_plan": stage1.stage1_plan,
#                     "mail_from": stage1.mail_from,
#                     "mail_to": stage1.mail_to,
#                     "selected_date": stage1.selected_date,
#                     "selected_comment_date": stage1.selected_comment_date,
#                     "stage1_report": stage1.stage1_report,
#                     "comment": stage1.comment
#                 },
#                 "stage2": None  # Placeholder to be updated later
#             })

#         # Process Stage 2 data and match with Stage 1
#         for stage2 in stage2_data:
#             found = False
#             for app in applications:
#                 if app["organisation_name"] == stage2.organisation_name and app["user_id"] == stage2.user_id:
#                     app["stage2"] = {
#                         "id": stage2.id,
#                         "scope": stage2.scope,
#                         "stage2_plan": stage2.stage2_plan,
#                         "mail_from": stage2.mail_from,
#                         "mail_to": stage2.mail_to,
#                         "selected_date": stage2.selected_date,
#                         "selected_comment_date": stage2.selected_comment_date,
#                         "stage2_report": stage2.stage2_report,
#                         "comment": stage2.comment
#                     }
#                     found = True
#                     break

#             # If no Stage 1 entry was found, create a new entry with only Stage 2 data
#             if not found:
#                 applications.append({
#                     "organisation_name": stage2.organisation_name,
#                     "user_id": stage2.user_id,
#                     "stage1": {},  # No Stage 1 record for this user
#                     "stage2": {
#                         "id": stage2.id,
#                         "scope": stage2.scope,
#                         "stage2_plan": stage2.stage2_plan,
#                         "mail_from": stage2.mail_from,
#                         "mail_to": stage2.mail_to,
#                         "selected_date": stage2.selected_date,
#                         "selected_comment_date": stage2.selected_comment_date,
#                         "stage2_report": stage2.stage2_report,
#                         "comment": stage2.comment
#                     }
#                 })

#             print("applications:", applications)
#             print(type(applications))

#         return jsonify({"applications": applications}), 200

#     except Exception as e:
#         print(f"Admin error fetching applications: {str(e)}")  # Debugging log
#         return jsonify({"error": str(e)}), 500


@app.route("/decision/application/<string:organisation_name>", methods=["GET"])
def decision_get_application_details(organisation_name):
    try:
        # Fetch matching records
        stage1_data = Stage1.query.filter(
            Stage1.organisation_name.ilike(organisation_name)).all()
        stage2_data = Stage2.query.filter(
            Stage2.organisation_name.ilike(organisation_name)).all()
        dashboard_data = Dashboard.query.filter(
            Dashboard.org_name.ilike(organisation_name)).all()

        if not stage1_data and not stage2_data and not dashboard_data:
            return jsonify({"message": f"No data found for organisation '{organisation_name}'"}), 404

        applications = []

        # Process Stage 1 data
        for stage1 in stage1_data:
            applications.append({
                "organisation_name": stage1.organisation_name,
                "user_id": stage1.user_id,
                "stage1": {
                    "id": stage1.id,
                    "scope": stage1.scope,
                    "stage1_plan": stage1.stage1_plan,
                    "mail_from": stage1.mail_from,
                    "mail_to": stage1.mail_to,
                    "selected_date": stage1.selected_date,
                    "selected_comment_date": stage1.selected_comment_date,
                    "stage1_report": stage1.stage1_report,
                    "comment": stage1.comment
                },
                "stage2": None,
                "zip_file_name": None
            })

        # Process Stage 2 data
        for stage2 in stage2_data:
            found = False
            for app in applications:
                if app["organisation_name"] == stage2.organisation_name and app["user_id"] == stage2.user_id:
                    app["stage2"] = {
                        "id": stage2.id,
                        "scope": stage2.scope,
                        "stage2_plan": stage2.stage2_plan,
                        "mail_from": stage2.mail_from,
                        "mail_to": stage2.mail_to,
                        "selected_date": stage2.selected_date,
                        "selected_comment_date": stage2.selected_comment_date,
                        "stage2_report": stage2.stage2_report,
                        "comment": stage2.comment
                    }
                    found = True
                    break

            if not found:
                applications.append({
                    "organisation_name": stage2.organisation_name,
                    "user_id": stage2.user_id,
                    "stage1": None,
                    "stage2": {
                        "id": stage2.id,
                        "scope": stage2.scope,
                        "stage2_plan": stage2.stage2_plan,
                        "mail_from": stage2.mail_from,
                        "mail_to": stage2.mail_to,
                        "selected_date": stage2.selected_date,
                        "selected_comment_date": stage2.selected_comment_date,
                        "stage2_report": stage2.stage2_report,
                        "comment": stage2.comment
                    },
                    "zip_file_name": None
                })

        # Process Dashboard data and add zip file details
        for dashboard in dashboard_data:
            for app in applications:
                if app["organisation_name"] == dashboard.org_name and app["user_id"] == dashboard.user_id:
                    app["zip_file_name"] = dashboard.zip_file_name
                    break
            else:
                # If no stage1/stage2 but only zip file exists, add it separately
                applications.append({
                    "organisation_name": dashboard.org_name,
                    "user_id": dashboard.user_id,
                    "stage1": None,
                    "stage2": None,
                    "zip_file_name": dashboard.zip_file_name
                })

        # Debugging output
        print("Retrieved applications:", applications)

        return jsonify({"applications": applications}), 200

    except Exception as e:
        print(f"Error fetching applications: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/stage2-prefill", methods=["GET"])
@jwt_required()
def stage2_prefill():
    user_email = get_jwt_identity()
    user = User.query.filter_by(email=user_email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    audit_number = request.args.get("audit_number")
    if not audit_number:
        return jsonify({"error": "Audit number required"}), 400

    stage1 = Stage1.query.filter_by(
        audit_number=audit_number,
        user_id=user.id
    ).first()

    if not stage1:
        return jsonify({"error": "Stage 1 data not found"}), 404

    return jsonify({
        "organisationName": stage1.organisation_name,
        "scope": stage1.scope or ""
    }), 200

if __name__ == "__main__":
    app.run(debug="True")
