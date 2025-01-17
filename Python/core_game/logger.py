from graphics import WHITE

log_messages = []


def log_event(message, color=WHITE):
    global log_messages

    log_messages.append({"message": message, "color": color, "current_frame": 0})
    
    if len(log_messages) > 10:
        log_messages.pop(0)

def clear_logs():
    global log_messages
    log_messages = []