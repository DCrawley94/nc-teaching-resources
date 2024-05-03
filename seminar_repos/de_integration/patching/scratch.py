from unittest.mock import MagicMock, patch

# conn = Connection(
#         host='localhost',
#         user='danika',
#         database='nc_games'
#     )

# print(Connection, ' <<< class')
# print(conn, ' <<< instance')
# print(Connection.run, ' <<< class method')
# print(conn.run, ' <<< instance method')
# print(Connection.run is conn.run, ' <<< class method is instance method? 😱')


from pg8000.native import Connection

conn = Connection(
        host='localhost',
        user='danika',
        database='nc_games'
    )

print(Connection, ' <<< class')
print(conn, ' <<< instance')
print(Connection.run, ' <<< class method')
print(conn.run, ' <<< instance method')
print(Connection.run is conn.run, ' <<< class method is instance method? 😱')

# with patch("pg8000.native.Connection.run", return_value=[[1,2,3]]) as mc:
#     conn = Connection(
#         host='localhost',
#         user='danika',
#         database='nc_games'
#     )
#     print(Connection, ' <<< class')
#     print(conn, ' <<< instance')
#     print(Connection.run, ' <<< class method')
#     print(conn.run, ' <<< instance method')
#     print(Connection.run is conn.run, ' <<< class method is instance method? 😱')
