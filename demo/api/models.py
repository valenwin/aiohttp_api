from gino import Gino


db = Gino()


class Cars(db.Model):
    __tablename__ = 'cars'
    __table_args__ = db.UniqueConstraint('vin_code')

    id = db.Column(db.Integer(), primary_key=True)
    producer = db.Column(db.String(150))
    model = db.Column(db.String(150))
    color = db.Column(db.String(150))
    year = db.Column(db.Integer())
    vin_code = db.Column(db.String(255))


async def main():
    await db.set_bind('postgresql://postgres:Tinka140792@localhost/demo_auto')
    await db.gino.create_all()
