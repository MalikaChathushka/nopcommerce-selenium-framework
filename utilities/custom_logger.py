import logging

class Log_Maker():
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",   # Log file path
            format='%(asctime)s: %(levelname)s: %(message)s',  # Log message format
            datefmt='%Y-/%m-/%d %H:%M:%S',            # Date and time format in logs
            force=True                              # Overrides any previous logging configs
        )

        # Get the root logger
        logger = logging.getLogger()

        # Set the minimum logging level to INFO (can be DEBUG, WARNING, ERROR, etc.)
        logger.setLevel(logging.INFO)

        # Return the logger object to use it elsewhere
        return logger