
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

def exists_in(column1, column2):
    """Determines whether the first set of results exists in the second set.
    
    INPUT:
    column1 & column2: The single-column results of a SQLAlchemy query.
    """

    return None
