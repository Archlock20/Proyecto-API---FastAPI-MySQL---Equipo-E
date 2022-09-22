from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/estudiantesdb")

meta = MetaData()

conn = engine.connect()