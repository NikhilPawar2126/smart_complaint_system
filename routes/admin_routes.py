from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Complaint, User

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
@login_required
def require_admin():
    if current_user.role != 'admin':
        flash('Unauthorized access.', 'error')
        return redirect(url_for('user.dashboard'))

@admin_bp.route('/dashboard')
def dashboard():
    total_users = User.query.filter_by(role='user').count()
    total_complaints = Complaint.query.count()
    pending = Complaint.query.filter_by(status='Pending').count()
    in_progress = Complaint.query.filter_by(status='In Progress').count()
    resolved = Complaint.query.filter_by(status='Resolved').count()
    
    return render_template('admin/dashboard.html', 
                           total_users=total_users,
                           total_complaints=total_complaints,
                           pending=pending,
                           in_progress=in_progress,
                           resolved=resolved)

@admin_bp.route('/complaints')
def complaints():
    status_filter = request.args.get('status')
    category_filter = request.args.get('category')
    
    query = Complaint.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    if category_filter:
        query = query.filter_by(category=category_filter)
        
    complaints_list = query.order_by(Complaint.created_at.desc()).all()
    return render_template('admin/complaints.html', complaints=complaints_list)

@admin_bp.route('/complaint/<int:complaint_id>/update', methods=['POST'])
def update_status(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    new_status = request.form.get('status')
    if new_status in ['Pending', 'In Progress', 'Resolved']:
        complaint.status = new_status
        db.session.commit()
        flash(f'Complaint #{complaint.id} status updated to {new_status}.', 'success')
    return redirect(url_for('admin.complaints'))

@admin_bp.route('/complaint/<int:complaint_id>/delete', methods=['POST'])
def delete_complaint(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    db.session.delete(complaint)
    db.session.commit()
    flash(f'Complaint #{complaint.id} deleted successfully.', 'success')
    return redirect(url_for('admin.complaints'))
