from models.course import Course


class CourseController:

    def __init__(self):
        """

        """
        print("Course controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("return all courses")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one course")

    def create(self, course_: dict) -> dict:
        """

        :param course_:
        :return:
        """
        print("insert course")

    def update(self, id_, course_: dict) -> dict:
        """

        :param id_:
        :param course_:
        :return:
        """
        print("update course")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete course")
