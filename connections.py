from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# SQLAlchemy needs an 'engine' (i.e. a connection) and a session for initialisation.

class MMSIMIGRATION():
    conn = \
    create_engine(
        'mssql+pyodbc://@MMSIMIGRATION/REBGVextra\
        ?trusted_connection=yes\
        &driver=ODBC+Driver+17+for+SQL+Server'
    )

    Session = sessionmaker(bind=conn)
    session = Session()



class SCRIBE_DEV1():
    conn = \
    create_engine(
        'mssql+pyodbc://@SCRIBE_DEV1/CRM_DATAMIGRATION2_STG_E2E\
        ?trusted_connection=yes\
        &driver=ODBC+Driver+17+for+SQL+Server'
    )

    Session = sessionmaker(bind=conn)
    session = Session()

