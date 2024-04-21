import yaml


class SingletonConfigLoader:
    """Singleton class to load configuration from a YAML file."""
    _instance = None

    def __new__(cls, config_file = None):
        """Creates a new instance or returns the existing singleton instance."""
        if not cls._instance:
            cls._instance = super(SingletonConfigLoader, cls).__new__(cls)
            cls._instance.config = None
            cls._instance.config_file = config_file
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        """Loads configuration data from the specified YAML file."""
        try:
            with open(self.config_file, 'r') as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            raise Exception(f"Configuration file not found: {self.config_file}")

    def get_value(self, path):
        """Retrieves a configuration value from a specific path within the YAML data."""
        try:
            config_path = path.split('.')
            result = self.config
            for item in config_path:
                result = result[item]
                
            return result
        except (KeyError, IndexError) as e:
            raise ValueError(f"Error retrieving configuration value: {e}")
