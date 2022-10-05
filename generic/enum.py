from enum import Enum


class GenericEnum(Enum):
    @classmethod
    def to_choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def get_name_list(cls):
        return tuple(i.name for i in cls)

    @classmethod
    def get_value_list(cls):
        return tuple(i.value for i in cls)
