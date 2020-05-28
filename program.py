from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLAlchemy needs an 'engine' (i.e. a connection) and a session in order to initialise.

class Connection():
    conn = \
    create_engine(
        'mssql+pyodbc://@MMSIMIGRATION/REBGVextra\
        ?trusted_connection=yes\
        &driver=ODBC+Driver+17+for+SQL+Server'
    )

    Session = sessionmaker(bind=conn)
    session = Session()

