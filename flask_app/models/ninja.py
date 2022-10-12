from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']
        self.age = data['age']

    @classmethod
    def get_all(cls, dojo):
        query = 'SELECT * FROM ninjas WHERE dojos_id = %(id)s'
        ninjas_from_dojo = connectToMySQL('dojos_and_ninjas').query_db(query, dojo)
        ninjas = []
        for ninja in ninjas_from_dojo:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, ninja):
        query = 'INSERT INTO ninjas (first_name, last_name, dojos_id, age) VALUES (%(first_name)s, %(last_name)s, %(dojos_id)s, %(age)s);'
        connectToMySQL('dojos_and_ninjas').query_db(query, ninja)

