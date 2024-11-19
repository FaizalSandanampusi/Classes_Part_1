class SmartDevice:
    """A class to represent a smart device.

    This class tracks the number of smart devices created and provides
    methods to manage their status and information.
    """

    # Class attribute to track total number of devices
    device_count = 0
    
    def __init__(self, device_name: str, model_number: str):
        """Initialize a new SmartDevice instance.

        Parameters
        ----------
        device_name : str
            The name of the device.
        model_number : str
            The model number of the device.

        Raises
        ------
        ValueError
            If the device name or model number is empty.
        """
        if not device_name or not model_number:
            raise ValueError("Device name and model number cannot be empty.")
        
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = False
        self.status = {}
        
        # Increment device count when new instance is created
        SmartDevice.device_count += 1
        
        # Initialize device_info as a lambda function
        self.device_info = lambda: {"name": self.device_name, "model": self.model_number}
    
    def update_status(self, attribute: str, value: any):
        """Update or add a status attribute with the given value.

        Parameters
        ----------
        attribute : str
            The name of the status attribute to update or add.
        value : any
            The value to set for the status attribute.

        Notes
        -----
        If the attribute already exists, its value will be updated.
        """
        self.status[attribute] = value
    
    def get_status(self, attribute: str) -> any:
        """Get the value of a status attribute.

        Parameters
        ----------
        attribute : str
            The name of the status attribute to retrieve.

        Returns
        -------
        any
            The value of the status attribute, or 'Attribute not found' if it does not exist.
        """
        return self.status.get(attribute, 'Attribute not found')
    
    def toggle_online(self):
        """Toggle the online status of the device."""
        self.is_online = not self.is_online
    
    def reset(self):
        """Reset all status attributes to default values.
        """
        self.status = {}
    
    def __call__(self) -> str:
        """Return device information as a string.

        Returns
        -------
        str
            A string representation of the device, including its name
            and model number.
        """
        return f"{self.device_name} (Model: {self.model_number})"

    def __str__(self) -> str:
        """Return a string representation of the device.

        Returns
        -------
        str
            A string representation of the SmartDevice instance.
        """
        return f"SmartDevice(name={self.device_name}, model={self.model_number}, online={self.is_online})"

    def __del__(self):
        """Decrement device count when an instance is deleted."""
        SmartDevice.device_count -= 1