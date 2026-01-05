'''from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video Downloaded Successfully!")


    except Exception as e:
        print(e) 

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a Youtube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Download Started....")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")'''


from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def save_video(url,file_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        high_resolution = streams.get_highest_resolution()
        high_resolution.download(output_path = file_path)
        print("The video has been downloaded successfully!")

    except Exception as e:
        print(e)

def folder_selector():
    folder = filedialog.askdirectory()
    if folder:
        print(f"The selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the URL of your Youtube video")

    save_dir = folder_selector()

    if save_dir:
        print('The video download is in progress..')
        save_video(video_url,save_dir)

    else:
        print('Invalid file path')





        

