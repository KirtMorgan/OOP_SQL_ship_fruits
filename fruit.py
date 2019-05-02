from db_connection_wrapper import *


class Fruit:

    def __init__(self, type='', kg='', grade='', treated='', expiration_date=''):
        self.type_of_fruit = type
        self.kg_of_fruit = kg
        self.grade = grade
        self.treated = treated
        self.expiration_date = expiration_date

    def read_all(self):
        try:
            fruits = sql_query_no_transaction("SELECT * FROM fruit")
            for fruit in fruits:
                print(f"Fruit: {fruit.type_of_fruit}\nWeight: {fruit.kg_of_fruit.strip()}\nGrade: {fruit.grade}\nFruit Treated: {fruit.treated}\nExpiration Date: {fruit.expiration_date}")
                Fruit(fruit.type_of_fruit, fruit.kg_of_fruit, fruit.grade, fruit.treated, fruit.expiration_date)
            print('Operation complete, read successful')

        except Exception as errmsg:
                print('There has been a error the record(s) have not been read, please see below exception message')
                print(errmsg)

    def save(self,type_of_fruit, kg_of_fruit, grade, treated, expiration_date):
        try:
            sql_query_no_transaction(f"INSERT INTO fruit(type_of_fruit, kg_of_fruit, grade, treated, expiration_date) VALUES('{type_of_fruit}', {kg_of_fruit}, '{grade}', '{treated}', '{expiration_date}');")
            docker_shipping_fruit.commit()
            print('The table has been updated, 1 row affected')

        except Exception as errmsg:
            print('There has been a error the record has not been committed, please see below exception message')
            print(errmsg)