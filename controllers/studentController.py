from models.student import Student


class StudentController:

    def __init__(self):
        """
        This is the constructor of the StudentController class
        """
        print("Student Controller ready")

    def index(self) -> list:
        """
        This method returns all students persisted in the db
        :return: student's list
        """
        print("return all students")
        data = {
            "_id": "abc123",
            "personal_id": "123456",
            "names": "Pepita",
            "lastname": "Perez"
        }
        student = Student(data)
        return [student.__dict__]

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one student")
        data = {
            "_id": id_,
            "personal_id": "123456",
            "names": "Pepita",
            "lastname": "Perez"
        }
        student = Student(data)
        return student.__dict__

    def create(self, student_: dict) -> dict:
        """

        :param student_:
        :return:
        """
        print("insert a student")
        student = Student(student_)
        return student.__dict__

    def update(self, id_: str, student_: dict) -> dict:
        """
        :param id_:
        :param student_:
        :return:
        """
        print("update a student")
        data = student_
        data['_id'] = id_
        student = Student(data)
        return student.__dict__

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete student " + id_)
        return {"Delete count": 1}
