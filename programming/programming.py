import argparse
import subprocess
import webbrowser

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--all", action="store_true", help='Run all programms')

args = parser.parse_args()
print(args)

if args.all == True:
    webbrowser.open('https://music.yandex.kz/users/CleRleQ/playlists/3', new=0)
    webbrowser.open('https://docs.djangoproject.com/en/4.0/', new=0)
    try: 
        url = 'C:\\Users\\Atomniy-PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Cods.exe'
        subprocess.Popen(url)
    except FileNotFoundError:
        print(f"ERROR!!! \n VS Code not found. Used path: '{url}' .")
