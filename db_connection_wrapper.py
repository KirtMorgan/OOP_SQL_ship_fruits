import pyodbc

connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'shipping_fruit'
username = 'SA'
password = 'Passw0rd2018'

docker_shipping_fruit = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = docker_shipping_fruit.cursor()


def sql_query_no_transaction(sql_query):
    return cursor.execute(sql_query)