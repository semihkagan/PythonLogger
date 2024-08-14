from lib.Logger import Logger

logger = Logger(stack_mode=True, ConsolePrnt=True, file_name="app.log", logs_folder="app_logs")

logger.log("This is a general log message.")
logger.info("This is an informational message.")
logger.err("This is an error message.", "IOError")
logger.warn("This is a warning message.", "DeprecationWarning")

# Clear all logs
if logger.clear():
    print("All logs cleared.")
    
