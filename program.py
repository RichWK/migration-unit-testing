from sqlalchemy.sql import exists

def is_not_null(data, column):
    """Determines whether the provided column contains any null values.
    
    INPUT:
    data: This should be the results of a SQLAlchemy query.
    column: A string specifying the table and column name, separated with only a period.

    OUTPUT:
    Boolean value.
    """

    if data.filter(column == None).first() == None:
        return True
    else:
        return False



def missing_from_target(source_column, target_column, primary_session, session2 = None):
    """Determines whether the values from the source column exist in the target column.
    
    INPUT:
    source_column: The values to be verified, in the format of tablename.columnname
    target_column: The name of the column which values will be verified against.
    primary_session: This determines the connection used. (See connections.py.)
    session2: This is used as the connection for 'target_column' if provided.

    OUTPUT:
    An integer with a count of the number of missing records.
    """

    # Default session2 to the primary_session (only if session2 hasn't been provided).

    session2 = primary_session if session2 == None else session2

    source_data = primary_session.query(source_column)
    target_data = session2.query(target_column)

    missing_records = 0

    # The '~' operator negates the exists() call.

    for record in source_data.filter(~exists().where(source_column==target_column)):
        missing_records += 1

    return missing_records



def duplicates_exist(session, column):
    """Determines if any duplicates exist in the provided column."""
    
    data = session.query(column)
    count = data.count()
    distinct_count = data.distinct().count()

    if distinct_count != count:
        return True
    else:
        return False

