from datetime import datetime


def run_and_log(func):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        result = func()

        if result is not None:
            log_message = (f"{timestamp} - {func.__name__} ran successfully:"
                           f" {result}")
        else:
            log_message = f"{timestamp} - {func.__name__} ran successfully"
    except Exception as e:
        log_message = f"{
            timestamp} - {func.__name__} encountered an error: {str(e)}"

    return log_message
