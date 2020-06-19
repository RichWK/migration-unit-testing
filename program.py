from os import getcwd
from sqlalchemy.sql import or_, exists



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



def missing_from_target(source_column, target_column, session, target_column2 = None):
    """Determines whether the values from the source column exist in the target column.
    Nulls values in the source column are ignored.
    
    INPUT:
    source_column: The values to be verified, in the format of tablename.columnname
    target_column: The name of the column which values will be verified against.
    session: This determines the connection used. (See connections.py.)
    target_column2: If supplied, also checks a second column for values which might not
        be contained in the first.

    OUTPUT:
    An integer with a count of the number of distinct missing records.
    """

    data = session.query(source_column).distinct().filter(source_column.isnot(None))
    logic = source_column==target_column

    # If a second target column is provided, the values can be found in either.

    if target_column2 is not None:
        logic = or_(source_column==target_column,source_column==target_column2)

    missing_records = 0
    
    # The '~' operator negates the exists() call.

    for record in data.filter(~exists().where(logic)):
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



# def write_to_file(data):

#     file_data = str()
        
#     for record in data:
#         file_data += record + '\n'

#     with open('test.txt', 'w') as file:
#         file.write(file_data)

