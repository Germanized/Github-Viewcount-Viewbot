import customtkinter as ctk
import requests
import threading
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ProfileViewer:
    def __init__(self, output_box):
        self.counter = 0
        self.output_box = output_box

    def view_profile(self, url: str):
        url = url.strip()
        requests.get(url)
        self.counter += 1

        self.output_box.insert(ctk.END, f"GitHub view counter: +{self.counter}\n")
        self.output_box.see(ctk.END)

    def boost_views(self, url, views):
        start_time = time.time()
        for _ in range(views):
            self.view_profile(url)
        end_time = time.time()

        time_elapsed = end_time - start_time
        self.output_box.insert(ctk.END, f"Completed boosting in {time_elapsed:.2f} seconds!\n")
        self.output_box.insert(ctk.END, f"Your GitHub account has now an extra {views} views!\n")
        self.output_box.see(ctk.END)

def start_boost(profile_viewer, url_entry, views_entry):
    url = url_entry.get().strip()
    views = int(views_entry.get().strip())

    profile_viewer.output_box.delete(1.0, ctk.END)

    threading.Thread(target=profile_viewer.boost_views, args=(url, views)).start()

app = ctk.CTk()
app.title("GitHub Profile View Booster By Germanized")
app.geometry("500x400")

url_label = ctk.CTkLabel(app, text="GitHub Profile URL:")
url_label.pack(pady=10)

url_entry = ctk.CTkEntry(app, width=400)
url_entry.pack(pady=10)

views_label = ctk.CTkLabel(app, text="Number of Views:")
views_label.pack(pady=10)

views_entry = ctk.CTkEntry(app, width=400)
views_entry.pack(pady=10)

output_box = ctk.CTkTextbox(app, width=450, height=150)
output_box.pack(pady=10)

profile_viewer = ProfileViewer(output_box)

boost_button = ctk.CTkButton(app, text="Boost Views", command=lambda: start_boost(profile_viewer, url_entry, views_entry))
boost_button.pack(pady=20)

app.mainloop()
