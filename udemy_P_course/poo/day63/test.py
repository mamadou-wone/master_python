from database import db, Books

db.create_all()
# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')
#
# db.session.add(admin)
# db.session.add(guest)
db.session.commit()

boss = Books.query.filter_by(username='guest').first()
print(boss.email)
# print(User.query_all())