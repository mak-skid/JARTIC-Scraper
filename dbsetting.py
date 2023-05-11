from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

host= os.getenv("HOST"),
user=os.getenv("USERNAME"),
passwd= os.getenv("PASSWORD"),
db= os.getenv("DATABASE"),
ssl_mode = "VERIFY_IDENTITY",
ssl      = {
    "ca": "/etc/ssl/cert.pem"
}

ENGINE = create_engine( #connect to database
    f"mysql+mysqlconnector://{user}:{passwd}@{host}/{db}?ssl_mode={ssl_mode}",
    connect_args={"ssl": ssl},
)
session = scoped_session(sessionmaker(bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()