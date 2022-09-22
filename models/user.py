from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


users = Table("users", meta, 
    Column("id", Integer, primary_key=True), 
    Column("cedula", String(10)), 
    Column("name", String(100)), 
    Column("lastname", String(100)),
    Column("age", String(3)),
    Column("email", String(100)),
    Column("gender", String(2)),
    Column("password", String(255)))

meta.create_all(engine)