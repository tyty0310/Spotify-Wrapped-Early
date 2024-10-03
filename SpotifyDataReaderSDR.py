import json
import os
from collections import defaultdict

def load_spotify_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except PermissionError:
        print(f"Error: Permission denied when trying to access '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def extract_artist_stats(data):
    artist_stats = defaultdict(lambda: {'plays': 0, 'minutes': 0})

    for entry in data:
        artist = entry.get('artistName', "").strip()
        ms_played = entry.get('msPlayed', 0)

        if artist.lower() == "unknown artist":
            artist = "Local Files"

        if artist:
            artist_stats[artist]['plays'] += 1
            artist_stats[artist]['minutes'] += ms_played / 60000  # Convert ms to minutes

    return artist_stats

def display_artist_stats(artist_stats, top_n=None):
    sorted_artists = sorted(artist_stats.items(), key=lambda x: x[1]['minutes'], reverse=True)

    if sorted_artists:
        print(f"{'Artist':<30}{'Plays':<10}{'Minutes Listened':<15}")
        print("-" * 55)

        if top_n:
            sorted_artists = sorted_artists[:top_n]

        for artist, stats in sorted_artists:
            print(f"{artist:<30}{stats['plays']:<10}{stats['minutes']:<15.2f}")

        print("-" * 55)
        print("Made With Love by TyPlant <3")

def main():
    os.system('title SpotifyDataReader (SDR)')

    file_path = input("Enter the path to your Spotify JSON file: ").strip('"')

    print(f"Attempting to open: {file_path}")

    data = load_spotify_data(file_path)

    if data is not None:
        artist_stats = extract_artist_stats(data)

        choice = input("Enter 1 for all artists or 2 for top 5 artists: ")

        if choice == '1':
            display_artist_stats(artist_stats)
        elif choice == '2':
            display_artist_stats(artist_stats, top_n=5)
        else:
            print("Invalid choice. Please enter 1 or 2.")

    input("\nPress Enter to close the program...")

if __name__ == "__main__":
    main()
