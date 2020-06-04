from sqlalchemy.sql import exists



def is_not_null(data, column):
    """Determines whether the provided column contains any null values.
    
    INPUT:
    data: This should be the results of a SQLAlchemy query.
    column: A string specifying the table and column name, separated with only a period.

    OUTPUT:
    Boolean value.
    """

    if data.filter(column is None).first() is None:
        return True
    else:
        return False



def missing_from_target(source_column, target_column, session):
    """Determines whether the values from the source column exist in the target column.
    Nulls values in the source column are ignored.
    
    INPUT:
    source_column: The values to be verified, in the format of tablename.columnname
    target_column: The name of the column which values will be verified against.
    primary_session: This determines the connection used. (See connections.py.)
    session2: This is used as the connection for 'target_column' if provided.

    OUTPUT:
    An integer with a count of the number of missing records.
    """

    missing_records = 0
    source_data = session.query(source_column).filter(source_column.isnot(None))

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

