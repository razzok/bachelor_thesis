# bachelor_thesis

### How to run
1. clone the repository
2. mkvirutalenv NAME -r requirements.txt
3. install caddy
4. add 127.0.0.1 bachelor.dev in your /etc/hosts
5. edit the Path in test_case.py for the Browsermob_Proxy and the path in routes.py to the static/push_manifest.json
6. cd in caddy - run caddy -conf Caddyfile
7. cd in bachelor_thesis - run gunicorn routes:app

Have fun visit bachelor.dev in your Browser
