# 📝 Python Logger - Simple Logging Utility 📝

This project is a Python-based logging utility designed to help developers easily log messages, warnings, errors, and info to a file with optional console output. The logger also supports file stacking, where log files can be compressed and moved to a designated folder. 📂

## Features ✨

- **Log Messages**: Easily log custom messages, information, warnings, and errors.
- **File Stacking**: Automatically compresses and moves log files to a specified folder.
- **Console Output**: Optionally print log messages to the console in color.
- **Clear Logs**: Provides the ability to clear all log files in the specified folder.

## Usage 🚀

### 1. Initialization 🛠️

You can initialize the `Logger` class with the following parameters:

- `stack_mode` (default: `False`): If `True`, it will compress the log file and move it to the specified `logs_folder`.
- `ConsolePrnt` (default: `True`): If `True`, it will print logs to the console.
- `file_name` (default: `"log.log"`): Name of the log file where messages will be stored.
- `logs_folder` (default: `"logs"`): Folder where compressed logs will be stored.

### 2. Logging Messages 📜

- **log(text)**: Logs a general message.
- **info(text)**: Logs an informational message with `[INFO]` tag.
- **err(text, err_type)**: Logs an error message with `[ERROR]` tag, optionally with a specific error type.
- **warn(text, warn_type)**: Logs a warning message with `[WARNING]` tag, optionally with a specific warning type.

### 3. Clearing Logs 🧹

- **clear()**: Deletes all files in the `logs_folder`.

### Example Usage 💡

```python
from logger import Logger

logger = Logger(stack_mode=True, ConsolePrnt=True, file_name="app.log", logs_folder="app_logs")

logger.log("This is a general log message.")
logger.info("This is an informational message.")
logger.err("This is an error message.", "IOError")
logger.warn("This is a warning message.", "DeprecationWarning")

# Clear all logs
if logger.clear():
    print("All logs cleared.")
```

### 4. Stack Mode 📦

If `stack_mode` is enabled, the log file is automatically compressed into a `.zip` file and moved to the `logs_folder` each time the logger is initialized.

## Requirements 🛠️

To run this script, you'll need the following library installed:

- `colorama`: Used for colored text in the terminal.

You can install it with the following command:

```bash
pip install colorama
```

## License 📜

This project is licensed under the [MIT License](LICENSE).

---

Developed with ❤️ by [Semih Kagan](https://github.com/semihkagan).
