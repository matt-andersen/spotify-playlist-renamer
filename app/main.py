import logging
import os
import sys

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Initialise logging:
logger = logging.getLogger()
logger.setLevel(int(os.environ.get("LOG_LEVEL")))
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s: in %(filename)s: %(message)s")
)
logger.addHandler(handler)


def main():
    logger.info("Running job")

    # Initialise connection to Spotify API:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-public playlist-modify-private",
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
            redirect_uri=os.environ.get("REDIRECT_URI"),
            cache_path=os.environ.get("CACHE_DIR"),
            open_browser=False,
        )
    )

    # Retrieve the playlist name:
    playlist_name = sp.playlist(os.environ.get("PLAYLIST_ID"))["name"]

    # Check playlist name, then change playlist name if appropriate:
    if playlist_name != os.environ.get("PLAYLIST_NAME"):
        logger.info(f"Renaming playlist back to {os.environ.get('PLAYLIST_NAME')}")
        sp.playlist_change_details(
            playlist_id=os.environ.get("PLAYLIST_ID"),
            name=os.environ.get("PLAYLIST_NAME"),
        )
    else:
        logger.info("No changes made")


if __name__ == "__main__":
    main()
