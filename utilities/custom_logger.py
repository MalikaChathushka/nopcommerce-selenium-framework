import logging  # Import the logging module to enable logging throughout the project

class Log_Maker():
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",   # Set the log file path where logs will be saved
            format='%(asctime)s: %(levelname)s: %(message)s',  # Define the format for log messages (timestamp, level, message)
            datefmt='%Y-/%m-/%d %H:%M:%S',            # Set the date and time format for log entries
            force=True                              # Force override any previous logging configuration to ensure consistency
        )

        # Get the root logger instance to configure logging globally
        logger = logging.getLogger()

        # Set the minimum logging level to INFO so that INFO and above messages are captured
        logger.setLevel(logging.INFO)

        return logger # Return the logger object so it can be used in other modules for