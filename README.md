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

# logo doesn't fit well in Read me's    

Welcome to the Germanized GitHub Booster!

Enter your GitHub views counter URL: Your view count url ex: https://camo.githubusercontent.com/ce40e20b925339267ea4f98ec4b1a3aae2707ce2cf2c48901030c29a45fdb2ee/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6765726d616e697a6564266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174
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
