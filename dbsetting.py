from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

HOST= os.getenv("HOST")
USER=os.getenv("USERNAME")
PASSWD= os.getenv("PASSWORD")
DB= os.getenv("DATABASE")
SSL_CA = "/etc/ssl/cert.pem"

ENGINE = create_engine( #connect to database
    f"mysql+mysqlconnector://{USER}:{PASSWD}@{HOST}/{DB}?ssl_verify_identity:{True}",
    connect_args={"ssl_ca": SSL_CA},
    echo=True
)
session = scoped_session(sessionmaker(bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()