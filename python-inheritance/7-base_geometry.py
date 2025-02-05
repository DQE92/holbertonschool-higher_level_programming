class BaseGeometry:
    """Base class for geometry with area method and integer validation."""

    def area(self):
        """
        Method that should calculate the area.
        However, it is not implemented in this base class.
        Raises an exception to enforce implementation in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Parameters:
        - name (str): The name of the parameter (assumed to be always a string).
        - value: The value to validate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is <= 0.
        """
        if not isinstance(value, int):  # Check if value is not an integer
            raise TypeError(f"{name} must be an integer")
        if value <= 0:  # Check if value is <= 0
            raise ValueError(f"{name} must be greater than 0")