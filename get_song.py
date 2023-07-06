import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify credentials
client_id = '73fc63c4c0b94bae956be3ebb6da0469'
client_secret = 'b559a55cec5b4f1c8ebea254e660e1ce'
market = 'ES'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for slow English romantic songs
results = sp.category_playlists(category_id='pop', country=market, limit=50)
playlists = results['playlists']['items']

# Retrieve tracks from each playlist
tracks = []
for playlist in playlists:
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    print(f"Playlist: {playlist_name}")
    print("Tracks:")
    playlist_tracks = sp.playlist_tracks(playlist_id)
    for track in playlist_tracks['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        album_name = track['track']['album']['name']
        release_year = track['track']['album']['release_date'][:4]
        popularity = track['track']['popularity']
        print(f"    {track_name} by {artist_name}")
        tracks.append([track_name, artist_name, album_name, release_year, popularity])

# Save the list of tracks as a CSV file
filename = 'spotify.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Track Name', 'Artist Name', 'Album', 'Year', 'Popularity'])
    writer.writerows(tracks)

print(f"\nData saved as {filename}")