# from pprint import pprint

# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# SPOTIFY_CLIENT_ID = ""
# SPOTIFY_CLIENT_SECRET = ""
# USER_ID = "1qvxredabar75l63gnvp7mpjm"
# REDIRECT_URI = "https://example.com"
# ENTIRE_ULR = "https://example.com/?code=AQCBb1vyB-4JbCuD6heMqQltUDiI9zpv26v34IMNknbTsu8KLrAQ-vaGVONy0-6E7eEtlsIlUC6FARBtclpnn6qy09yDal1IrnS4C82JMeUYJjeUWMWq9sBOxc2IGk4V6gevKCLqIc_4z42Fs8pLk0jX-91D-6LUKoYyt3_CfrqKaBUr2s_MckZL"
#
# date = input("Wich year do you want to travel to? "
#              "Type the date in this format YYYY-MM-DD: ")
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}"
# #
# response = requests.get(URL)
# website_content = response.text
#
# soup = BeautifulSoup(website_content, "html.parser")
#
# song_list = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
#
# top_music = [song.getText() for song in song_list]
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=f"{SPOTIFY_CLIENT_ID}",
#                                                client_secret=f"{SPOTIFY_CLIENT_SECRET}",
#                                                redirect_uri=f"{REDIRECT_URI}",
#                                                scope="playlist-modify-private"))
#
#
# # print(sp.current_user()['id'])
# #
# def get_url(song):
#     results = sp.search(q=f"{song}", limit=1)
#     for idx, track in enumerate(results['tracks']['items']):
#         return track['uri']
#
#
# url_list = []
# url = "http://open.spotify.com/track/"
#
# for song in top_music:
#     try:
#         url_list.append(f"{url}{get_url(song).split(':')[2]}")
#     except IndexError:
#         pass
#
# new_playlist = sp.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100",
#                                        public=False, collaborative=False,
#                                        description=f"The {date} Billboard 100"
#                                        )
#
#
# sp.playlist_add_items(playlist_id=f"{new_playlist['id']}", items=url_list)
