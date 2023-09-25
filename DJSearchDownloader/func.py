import requests
import os
import yt_dlp
from bs4 import BeautifulSoup
from sclib import SoundcloudAPI, Track
from youtubesearchpython import VideosSearch
#--------------------------------------------------------------------------------------------------
#                          FONCTION RECHERCHE SOUNDCLOUD
#--------------------------------------------------------------------------------------------------
def recherche_soundcloud(query):
    if query == "":
        return [],[]
    url = f"https://soundcloud.com/search/sounds?q={query}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Recherchez tous les éléments de type "li" qui contiennent les titres et les URL.
    search_results = soup.find_all('li')[5:10]
    url_list,title_list = list(),list()
    # Parcourez les résultats et extrayez le titre et l'URL de chaque recherche.
    for index, result in enumerate(search_results, start=1):
        """if index == 5:
            continue  # Passez au 7ème élément (indice 6)."""

        # Traitez le résultat ici comme d'habitude.
        title_elem = result.find('a')
        title = title_elem.text.strip()
        url = title_elem.get('href')
        url_list.append(url)
        title_list.append(title)
        duration = 0
        # Imprimez ou faites ce que vous voulez avec les données.
        print(f"Résultat {index}:")
        print(f"Titre: {title}")
        print(f"URL: {url}")
        print(f"Durée: {duration}")
        print()

    return url_list,title_list
#--------------------------------------------------------------------------------------------------
#                          FONCTION RECHERCHE YOUTUBE
#--------------------------------------------------------------------------------------------------
def recherche_youtube(query):
    # Effectuer la recherche sur YouTube
    videosSearch = VideosSearch(query, limit=5)
    results = videosSearch.result()

    # Initialiser des listes pour stocker les informations
    titles = []
    urls = []
    durations = []

    # Parcourir les résultats et extraire les informations
    for video in results['result']:
        title = video['title']
        url = f"https://www.youtube.com/watch?v={video['id']}"
        duration = video['duration']

        # Ajouter les informations aux listes respectives
        titles.append(title)
        urls.append(url)
        durations.append(duration)

    # Afficher les informations extraites
    for i in range(len(titles)):
        print(f"Titre : {titles[i]}")
        print(f"URL : {urls[i]}")
        print(f"Durée : {durations[i]}\n")
    return titles,urls,durations
# --------------------------------------------------------------------------------------------------
#                          FONCTION TELECHARGEMENT SOUNDCLOUD
# --------------------------------------------------------------------------------------------------
def download_soundcloud(url,titre,genre):
    api = SoundcloudAPI()
    track = api.resolve("https://soundcloud.com"+url)
    assert type(track) is Track
    filename = f'Download Music/{genre}/{titre}.mp3'

    with open(filename, 'wb+') as file:
        track.write_mp3_to(file)
# --------------------------------------------------------------------------------------------------
#                          FONCTION TELECHARGEMENT YOUTUBE
# --------------------------------------------------------------------------------------------------
def download_youtube_audio(url, titre, genre):
    print("EXECUTION")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac/alac',
        }],
        'outtmpl': f'Download Music/{genre}/{titre}',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            video = info['entries'][0]
        else:
            video = info

        # Vérifiez si le fichier existe déjà
        filename = f'Download Music/{genre}/{titre}.{video["ext"]}'
        if os.path.exists(filename):
            print(f"Le fichier {filename} existe déjà.")
            return

        # Téléchargez la vidéo
        ydl.download([url])
        print(f"La vidéo a été téléchargée avec succès sous le nom {filename}")
# --------------------------------------------------------------------------------------------------
#                                       AUTRES
# --------------------------------------------------------------------------------------------------
