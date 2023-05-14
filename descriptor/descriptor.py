class Validator:
    """Descriptor class

     checks if the first letter of the full name is capitalized and if the full name contains only letters."""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, name):
        self.validate_name(name)
        setattr(instance, self.param_name, name)

    def __delete__(self, instance):
        raise AttributeError(f"Attribute {self.param_name} cannot be deleted")

    @staticmethod
    def validate_name(value: str):
        if not value.isalpha():
            raise ValueError(f'Name "{value}" should contain only alpha characters')
        elif not value[0].isupper():
            raise ValueError(f'First character in "{value}" must be a title character')