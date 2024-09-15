import requests
import time
import random
import colorama
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed

colorama.init(autoreset=True)
print(f"{Fore.YELLOW}GitHub View Booster By Germanized")

class ProfileViewer:
    def __init__(self):
        self.counter = 0
        self.success_count = 0
        self.error_count = 0
        self.paused = False

    def view_profile(self, url: str):
        url = url.strip()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        retry_attempts = 3
        for attempt in range(retry_attempts):
            if self.paused:
                self.handle_pause()
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    self.counter += 1
                    self.success_count += 1
                    self.update_status(f"{Fore.GREEN}Status: Views Sent ({self.counter})")
                    return
                else:
                    self.error_count += 1
                    self.update_status(f"{Fore.YELLOW}Status: Response status: {response.status_code}")
            except requests.RequestException as e:
                self.error_count += 1
                with open("error_log.txt", "a") as log_file:
                    log_file.write(f"Error: {e}\n")
                self.update_status(f"{Fore.RED}Status: Error: {e}")
            
            self.paused = True
            self.handle_pause()
            self.paused = False
        self.update_status(f"{Fore.RED}Status: Failed after {retry_attempts} attempts")

    def handle_pause(self):
        time.sleep(120)
        self.update_status(" " * 60)

    def update_status(self, status_message):
        print(status_message, end='\r')

    def boost_views(self, url, views):
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.view_profile, url) for _ in range(views)]
            for future in as_completed(futures):
                pass
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"\n{Fore.CYAN}Completed boosting in {time_elapsed:.2f} seconds!")
        print(f"{Fore.GREEN}Your GitHub account has now an extra {self.counter} views!")
        print(f"{Fore.YELLOW}Total successful requests: {self.success_count}")
        print(f"{Fore.RED}Total errors: {self.error_count}\n")

def main_menu():
    logo = r"""
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
"""
    print(f"{Fore.YELLOW}{logo}")
    print(f"{Fore.CYAN}Welcome to the Germanized GitHub Booster!\n")
    print(f"{Fore.MAGENTA}[1] Boost GitHub Views")
    print(f"{Fore.MAGENTA}[2] Exit\n")

def start_boost():
    profile_viewer = ProfileViewer()
    url = input(f"{Fore.YELLOW}Enter your GitHub views counter URL: ").strip()
    views = int(input(f"{Fore.YELLOW}Enter the number of views you want: ").strip())
    profile_viewer.boost_views(url, views)

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input(f"{Fore.CYAN}Select an option: ").strip()
        if choice == "1":
            start_boost()
        elif choice == "2":
            print(f"{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please try again.")
