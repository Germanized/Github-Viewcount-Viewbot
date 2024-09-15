# GitHub View Booster by Germanized

This script is designed to boost the view count of a specific GitHub profile or repository by simulating view requests using Python. It supports multi-threading to increase efficiency and includes built-in error handling, retry logic, and a pause mechanism to avoid overloading.

## Features

- **Multi-threaded Requests**: Boost views quickly by sending multiple requests concurrently.
- **Error Handling**: Retries on failed attempts and logs errors in `error_log.txt`.
- **Pause Mechanism**: Automatically pauses for 2 minutes between retry attempts to prevent spamming.
- **Status Updates**: Displays real-time updates in the console, with color-coded messages using `colorama`.
- **Customizable View Count**: Specify the number of views to send during each run.

## Requirements

- **Python 3.x**
- **Dependencies**: Install the required libraries by running:

  `pip install requests colorama`

## Usage

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the script using Python:

  `python github_view_booster.py`

4. You will be prompted to enter:
   - **GitHub profile/repo URL**: The URL you want to boost views for.
   - **Number of views**: Specify how many views you want to send.

5. The script will begin sending views and display progress in the terminal.

## Example

$ python github_view_booster.py
GitHub View Booster By Germanized

 _______ _       _           _ 
(_______|_)  _  | |         | |
 _   ___ _ _| |_| |__  _   _| |__
| | (_  | (_   _)  _ \| | | |  _ \
| |___) | | | |_| | | | |_| | |_) )
 \_____/|_|  \__)_| |_|____/|____/

 ______                      
(____  \                    _ 
 ____)  ) ___   ___   ___ _| |_ _____  ____  
|  __  ( / _ \ / _ \ /___|_   _) ___ |/ ___) 
| |__)  ) |_| | |_| |___ | | |_| ____| |     
|______/ \___/ \___/(___/   \__)_____)_|     

Welcome to the Germanized GitHub Booster!

Enter your GitHub views counter URL: https://github.com/yourprofile
Enter the number of views you want: 500


## Output

- The script will display success and error messages during the run.
- Example status messages:
  - `[+] Views Sent (1)` — A view request was successfully sent.
  - `[-] Error: ConnectionError` — An error occurred while attempting to send a view.
  - `Paused For 2 Mins` — The script is paused for 2 minutes between retry attempts.

## Error Logging

- Any errors encountered during the execution are logged into `error_log.txt` for later review.

## Credits

This script was developed by **Germanized**.

---

**Disclaimer**: This script is for educational purposes only. Use it responsibly to avoid any potential abuse of services.
