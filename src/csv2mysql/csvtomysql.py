import pandas as pd
from sqlalchemy import create_engine

with open('auth', 'r') as auth_file:
    user = auth_file.readline().strip()
    password = auth_file.readline().strip()
    database = auth_file.readline().strip()

connection_url = f'mysql://{user}:{password}@localhost/{database}'
print(connection_url)
engine = create_engine(connection_url)
con = engine.connect()

number_chunks = 1
csv_data_frame = pd.read_csv('all_c_cpp_release2.0.csv', chunksize=10, encoding='ISO-8859-1', on_bad_lines='skip')

for chunk in csv_data_frame:
    try:
        # Coluna impede que todas as tuplas sejam salvas, não é usada, por isso removemos
        chunk = chunk.drop(columns=['files_changed'])
        chunk.to_sql(name='bigvul2', con=con, schema='bigvul', if_exists='append', chunksize=10)
        print(f'Number of rows inserted: {number_chunks}')
        number_chunks = number_chunks + 1
        con.commit()
    except Exception:
        pass

con.close()
