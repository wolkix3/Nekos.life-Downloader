# Nekos.life-Downloader

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f762a7ac35754d7da87412af9a610102)](https://app.codacy.com/app/wolkix3/Nekos.life-Downloader?utm_source=github.com&utm_medium=referral&utm_content=wolkix3/Nekos.life-Downloader&utm_campaign=Badge_Grade_Dashboard)

A script to download images from the site Nekos.life

To change the Content it is supposed to download you need to replace the `api_url` variable to the wanted URL in the `script.py`. The default is for nekos.
The script is done downloading the entire category when it stops downloading new files.

## Available URLs:

1. https://nekos.life/api/v2/img/neko
2. https://nekos.life/api/v2/img/ngif   
3. https://nekos.life/api/v2/img/pat
4. https://nekos.life/api/v2/img/hug
5. https://nekos.life/api/v2/img/fox_girl
6. https://nekos.life/api/v2/img/waifu
7. https://nekos.life/api/v2/img/tickle
8. https://nekos.life/api/v2/img/classic
9. https://nekos.life/api/v2/img/kemonomimi
10. https://nekos.life/api/v2/img/poke
11. https://nekos.life/api/v2/img/smug
12. https://nekos.life/api/v2/img/lizard
13. https://nekos.life/api/v2/img/feed
14. https://nekos.life/api/v2/img/wallpaper
15. https://nekos.life/api/v2/img/avatar
16. https://nekos.life/api/v2/img/holo
17. https://nekos.life/api/v2/img/baka
18. https://nekos.life/api/v2/img/kiss
19. https://nekos.life/api/v2/img/gecg
20. https://nekos.life/api/v2/img/slap

NSFW(18+) URLs are in the `nsfw` file

## Dependencies:
requests

shutil

## Warning
This script downloads the Pictures pretty fast (depending on your internet speed) and if you put it on your Desktop it might fully bloat it.
