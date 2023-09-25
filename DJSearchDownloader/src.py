from func import *
import ytdl
#--------------------------------------------------------------------------------------------------
#   TODO :
# * Recherche & téléchargement SOUNDCLOUD : FAIT
# * Recherche & téléchargement YOUTUBE : FAIT
# * Faire une GUI : EN COURS
# * Proteger des exceptions : EN COURS
# * Option avec ACCAPELLA : PAS FAIT
# * Afficher la durée de la chanson avant de télécharger : FAIT (QUE YT)
# * Afficher la qualité en Kpbs de la chanson avant de télécharger : PAS FAIT
# * Passer en multi-threading : PAS FAIT
# * Transformer les téléchargements en fonction (SOUNCLOUD) : FAIT
# * Transformer les téléchargements en fonction (YOUTUBE) : FAIT
# * Préécouter avant téléchargement : PAS FAIT
# * Afficher les miniatures : PAS FAIT
# * Afficher le nombre d'écoutes ou vues : PAS FAIT
# * Menu déroulant avec les dossiers ou ranger la musique téléchargé : FAIT
# * Système de file d'attente : PAS FAIT
#--------------------------------------------------------------------------------------------------
#                          EXECUTION
#--------------------------------------------------------------------------------------------------

def recherche_youtube_test(query):
    # Effectuer la recherche sur YouTube
    videosSearch = VideosSearch(query, limit=1)
    results = videosSearch.result()
    print(results)


if __name__ == "__main__":
    recherche = "One of a time tita lau"#input("Entrez votre recherche : ")
    recherche_youtube_test(recherche)
