import asyncio
import logging
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from .config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

log = logging.getLogger(__name__)

sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-read-currently-playing user-read-playback-state",
        cache_path=".spotify_cache",
    )
)

_NOT_PLAYING = "🎵 ɪ'ᴍ ɴᴏᴛ ʟɪsᴛᴇɴɪɴɢ ᴛᴏ ᴍᴜsɪᴄ ɴᴏᴡ."


def _ms_to_mmss(ms: int) -> str:
    s = ms // 1000
    return f"{s // 60}:{s % 60:02d}"


async def fetch_spotify() -> str:
    try:
        data = await asyncio.to_thread(sp.current_playback)
        if not data or not data.get("is_playing") or not data.get("item"):
            return _NOT_PLAYING
        item = data["item"]
        artist = item["artists"][0]["name"]
        track = item["name"]
        position = _ms_to_mmss(data["progress_ms"])
        return f"🎵 {artist} — {track} · {position}"
    except Exception as e:
        log.warning("spotify: %s", e)
        return _NOT_PLAYING

