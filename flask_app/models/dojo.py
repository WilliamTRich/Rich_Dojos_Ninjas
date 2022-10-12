from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos=[]
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, dojo):
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        dojo_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, dojo)
        return cls(dojo_from_db[0])