from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Auditors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# class Stage1(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     organisation_name = db.Column(db.String(255), nullable=False)
#     scope = db.Column(db.String(255))
#     stage1_plan = db.Column(db.String(255))
#     mail_from = db.Column(db.String(255))
#     mail_to = db.Column(db.String(255))
#     selected_date = db.Column(db.String(255))
#     selected_comment_date = db.Column(db.String(255))
#     stage1_report = db.Column(db.String(255))
#     comment = db.Column(db.Text)

class Stage1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    audit_number = db.Column(db.String(255), nullable=False)  # ✅ ADD
    organisation_name = db.Column(db.String(255), nullable=False)

    scope = db.Column(db.String(255))
    stage1_plan = db.Column(db.String(255))
    mail_from = db.Column(db.String(255))
    mail_to = db.Column(db.String(255))
    mail_to_report = db.Column(db.String(255))
    selected_date = db.Column(db.String(255))
    selected_comment_date = db.Column(db.String(255))
    stage1_report = db.Column(db.String(255))
    comment = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint('audit_number', 'user_id', name='uq_stage1_audit_user'),
    )


# class Stage2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     organisation_name = db.Column(db.String(255), nullable=False)
#     scope = db.Column(db.String(255), nullable=False)
#     stage2_plan = db.Column(db.String(255))
#     mail_from = db.Column(db.String(255), nullable=False)
#     mail_to = db.Column(db.String(255), nullable=False)
#     selected_date = db.Column(db.String(50), nullable=False)
#     selected_comment_date = db.Column(db.String(50))
#     stage2_report = db.Column(db.String(255))
#     comment = db.Column(db.Text)

class Stage2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    audit_number = db.Column(db.String(255), nullable=False)  # ✅ ADD
    organisation_name = db.Column(db.String(255), nullable=False)

    scope = db.Column(db.String(255), nullable=False)
    stage2_plan = db.Column(db.String(255))
    additional_data = db.Column(db.String(255))
    mail_from = db.Column(db.String(255), nullable=False)
    mail_to = db.Column(db.String(255), nullable=False)
    mail_to_report = db.Column(db.String(255))
    selected_date = db.Column(db.String(50), nullable=False)
    selected_comment_date = db.Column(db.String(50))
    stage2_report = db.Column(db.String(255))
    comment = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint('audit_number', 'user_id', name='uq_stage2_audit_user'),
    )


class Dashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    org_name = db.Column(db.String(255), nullable=False)
    audit_number = db.Column(db.String(255), nullable=False)
    auditor = db.Column(db.String(255), nullable=False)
    decision_maker = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    zip_file_name = db.Column(db.String(255), nullable=True)
