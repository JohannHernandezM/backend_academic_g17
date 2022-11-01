from models.enrollment import Enrollment


class EnrollmentController:

    def __init__(self):
        """

        """
        print("Enrollment controller ready")

    # Equivalent to 'all'
    def index(self) -> list:
        """

        :return:
        """
        print("return all enrollments")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one enrollment")

    def create(self, enrollment_: dict) -> dict:
        """

        :param enrollment_:
        :return:
        """
        print("insert enrollment")

    def update(self, id_, enrollment_: dict) -> dict:
        """

        :param id_:
        :param enrollment_:
        :return:
        """
        print("update enrollment")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete enrollment")
