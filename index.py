import pyautogui
import pyperclip
import time

def append_delimiter_to_each_line(text, delimiter=", "):
    """
    Appends a delimiter to the end of each line in the given text,
    except the last line.
    
    :param text: The input text with lines separated by newlines.
    :param delimiter: The delimiter to append to each line.
    :return: The text with the delimiter appended to each line.
    """
    lines = text.split('\n')
    processed_lines = [line + delimiter if line else line for line in lines[:-1]]
    processed_lines.append(lines[-1])  # Append the last line without the delimiter
    return ''.join(processed_lines)

# Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')  # Use 'command' instead of 'ctrl' on macOS

# Wait for clipboard to update
time.sleep(1)

# Read text from clipboard
copied_text = pyperclip.paste()

# Process the copied text
processed_text = append_delimiter_to_each_line(copied_text)

# Copy the processed text back to clipboard
pyperclip.copy(processed_text)

# Paste the processed text
pyautogui.hotkey('ctrl', 'v')  # Use 'command' instead of 'ctrl' on macOS
