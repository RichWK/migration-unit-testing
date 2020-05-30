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



# These are helper functions used by tests.

def is_not_null(results, column):
    """Determines whether the provided column contains any null values.
    
    INPUT:
    results: This argument should be the results of a SQLAlchemy query.
    column: A string specifying the table and column name, separated with only a period.
    """
    if results.filter(column == None).first() == None:
        return True
    else:
        return False

