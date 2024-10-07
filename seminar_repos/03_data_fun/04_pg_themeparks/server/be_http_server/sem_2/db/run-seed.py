from db.seed import seed 
from db.connection import create_connection 
from db.data.index import data 


try:
	seed(**data)
except Exception as e:
	print(e)
