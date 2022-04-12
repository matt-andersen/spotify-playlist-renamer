import logging
import os
import sys

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SCOPE = "playlist-modify-public playlist-modify-private"
PLAYLIST_ID = "5dZCTRD5inv8lWdVzCmVYb"
PLAYLIST_NAME = "Dad Rock Essentials"

logger = logging.getLogger()
logger.setLevel(int(os.environ.get("LOG_LEVEL")))
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s: in %(filename)s: %(message)s")
)
logger.addHandler(handler)


def main():
    logger.info("Running job")

    spotify_oauth = SpotifyOAuth(
        scope=SCOPE,
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
        redirect_uri=os.environ.get("REDIRECT_URI"),
    )

    if os.environ.get("ENVIRONMENT") == "prod":
        spotify_oauth.cache_path = "/tmp/.cache"

    sp = spotipy.Spotify(auth_manager=spotify_oauth)

    playlist_name = sp.playlist(PLAYLIST_ID)["name"]

    if playlist_name != PLAYLIST_NAME:
        logger.info(f"Renaming playlist back to {PLAYLIST_NAME}")
        sp.playlist_change_details(playlist_id=PLAYLIST_ID, name=PLAYLIST_NAME)
    else:
        logger.info("No changes made")


if __name__ == "__main__":
    main()
