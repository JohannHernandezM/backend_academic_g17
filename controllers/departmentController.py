from models.department import Department


class DepartmentController:

    def __init__(self):
        """

        """
        print("Department controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("return all departments")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one department")

    def create(self, department_: dict) -> dict:
        """

        :param department_:
        :return:
        """
        print("insert a department")

    def update(self, id_: str, department_: dict) -> dict:
        """

        :param id_:
        :param department_:
        :return:
        """
        print("update a department")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete a department")
