from app import DB, models
models.User.query.delete()
DB.session.commit()