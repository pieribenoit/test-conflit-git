import os
from glob import glob
import shutil

chemin = "/Users/body ben/Desktop/tri_fichiers_sources/docs"

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents",
              ".txt": "Documents"}

fichiers = glob(os.path.join(chemin, "*"))
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    dossier = extensions.get(extension)
    if dossier:
        chemin_dossier = os.path.join(chemin, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
        shutil.move(fichier, chemin_dossier)