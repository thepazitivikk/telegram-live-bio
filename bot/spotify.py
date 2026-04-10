import asyncio
import json
import logging
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from .config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

log = logging.getLogger(__name__)

_SCOPE = "user-read-currently-playing user-read-playback-state"
_CACHE = ".spotify_cache"
_NOT_PLAYING = "🎵 ɪ'ᴍ ɴᴏᴛ ʟɪsᴛᴇɴɪɴɢ ᴛᴏ ᴍᴜsɪᴄ ɴᴏᴡ."


def _build_auth() -> SpotifyOAuth:
    auth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=_SCOPE,
        cache_path=_CACHE,
        open_browser=False,
    )
    refresh_token = os.getenv("SPOTIPY_REFRESH_TOKEN", "")
    if refresh_token and not os.path.exists(_CACHE):
        auth.cache_handler.save_token_to_cache({
            "access_token": "",
            "token_type": "Bearer",
            "refresh_token": refresh_token,
            "expires_at": 0,
            "scope": _SCOPE,
        })
    return auth


sp = Spotify(auth_manager=_build_auth())


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
