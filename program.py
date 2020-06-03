def is_not_null(data, column):
    """Determines whether the provided column contains any null values.
    
    INPUT:
    data: This argument should be the results of a SQLAlchemy query.
    column: A string specifying the table and column name, separated with only a period.
    """

    if data.filter(column == None).first() == None:
        return True
    else:
        return False

# todo: see https://docs.sqlalchemy.org/en/13/orm/tutorial.html#using-exists

def exists_in_target(primary_session, source_column, target_column, session2 = None):
    """Determines whether the values from the source column exist in the target.
    
    INPUT:
    column1 & column2: The single-column results of a SQLAlchemy query.
    """

    # Default session2 to the primary_session if session2 is null.
    session2 = primary_session if session2 == None else session2

    source_data = primary_session.query(source_column)
    target_data = session2.query(target_column)

    return None

def duplicates_exist(session, column):
    """Determines if any duplicates exist in the provided column."""
    
    data = session.query(column)
    count = data.count()
    distinct_count = data.distinct().count()

    if distinct_count != count:
        return True
    else:
        return False

