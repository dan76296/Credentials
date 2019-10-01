from .configuration import Configuration


class ProjectName(Configuration):

    def __init__(self):
        Configuration.__init__(self)
        pass

    def get_username(self):
        return self.get_configuration_value(header, value)

    def get_password(self):
        return self.get_configuration_value(header, value)

