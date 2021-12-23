from abc import ABC, abstractmethod


class ICourse(ABC):
    """Interface of the course in software academy."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of the course."""
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str):
        """Set name of the course."""
        pass

    @property
    @abstractmethod
    def program(self) -> list:
        """Get program of the course."""
        pass

    @program.setter
    @abstractmethod
    def program(self, program: list):
        """Set program of the course."""
        pass


class ITeacher(ABC):
    """Interface of the teacher in software academy.

    Attributes:
        name: string representing teacher's name.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of the teacher."""
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str):
        """Set name of the teacher."""
        pass


class ICourseFactory(ABC):
    """Inerface of courses and teacher factory."""
    @abstractmethod
    def create_local_course(self, name: str, teacher, *program: str):
        """Create local course."""
        pass

    @abstractmethod
    def create_offsite_course(self, name: str, teacher, *program: str):
        """Create offsite course."""
        pass

    @abstractmethod
    def create_teacher(self, name: str):
        """Create teacher."""
        pass


class ILocalCourse(ICourse):
    """Interface of local course in software academy.

    Attributes:
        name: string representing name of the course.
        teacher: Teacher object that teaches on the course.
        program: strings with course topics.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of the local course."""
        pass

    @ICourse.name.setter
    @abstractmethod
    def name(self, name: str):
        """Set name of the local course."""
        pass

    @property
    @abstractmethod
    def program(self) -> list:
        """Get program of the local course."""
        pass

    @ICourse.program.setter
    @abstractmethod
    def program(self, program: list):
        """Set program of the local course."""
        pass


class IOffsiteCourse(ICourse):
    """Interface of offsite course in software academy.

    Attributes:
        name: string representing name of the course.
        teacher: Teacher object that teaches on the course.
        program: strings with course topics."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of the offsite course."""
        pass

    @ICourse.name.setter
    @abstractmethod
    def name(self, name: str):
        """Set name of the offsite course."""
        pass

    @property
    @abstractmethod
    def program(self) -> list:
        """Get program of the offsite course."""
        pass

    @ICourse.program.setter
    @abstractmethod
    def program(self, program: list):
        """Set program of the offsite course."""
        pass
