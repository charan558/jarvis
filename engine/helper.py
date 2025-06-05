import re
import os
import time
import eel

def extract_yt_term(command):
    #Define a regular espression pattern to capture the song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find the pattern in the command
    match = re.search(pattern, command,re.IGNORECASE)
    #if a match is found, extract the song name from the match object
    return match.group(1) if match else None

def extract_spotify_term(command):
    # Define a regular expression pattern to capture the song name for Spotify
    pattern = r'play\s+(.*?)\s+on\s+spotify'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

### 6. Make Helper Function to remove unwanted words from query


def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string


# #Example usage
# input_string = "make a phone call to Dad"
# words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', '']

# result = remove_words(input_string, words_to_remove)
# print(result)



# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')
