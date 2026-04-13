from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models import db, Complaint
import os
import uuid

user_bp = Blueprint('user', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'user':
        return redirect(url_for('admin.dashboard'))
        
    complaints = Complaint.query.filter_by(user_id=current_user.id).all()
    total = len(complaints)
    pending = sum(1 for c in complaints if c.status == 'Pending')
    in_progress = sum(1 for c in complaints if c.status == 'In Progress')
    resolved = sum(1 for c in complaints if c.status == 'Resolved')
    
    return render_template('user/dashboard.html', 
                           total=total, 
                           pending=pending, 
                           in_progress=in_progress, 
                           resolved=resolved,
                           recent_complaints=complaints[-5:][::-1])

@user_bp.route('/submit', methods=['GET', 'POST'])
@login_required
def submit_complaint():
    if current_user.role != 'user':
        return redirect(url_for('admin.dashboard'))
        
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        description = request.form.get('description')
        
        # Handle file upload
        image_filename = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                ext = file.filename.rsplit('.', 1)[1].lower()
                filename = secure_filename(f"{uuid.uuid4().hex}.{ext}")
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                image_filename = filename
                
        new_complaint = Complaint(
            title=title,
            category=category,
            description=description,
            image_filename=image_filename,
            user_id=current_user.id
        )
        
        db.session.add(new_complaint)
        db.session.commit()
        
        flash('Complaint submitted successfully.', 'success')
        return redirect(url_for('user.dashboard'))
        
    return render_template('user/submit.html')

@user_bp.route('/history')
@login_required
def history():
    if current_user.role != 'user':
        return redirect(url_for('admin.dashboard'))
        
    complaints = Complaint.query.filter_by(user_id=current_user.id).order_by(Complaint.created_at.desc()).all()
    return render_template('user/history.html', complaints=complaints)
