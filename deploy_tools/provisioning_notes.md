# Provisioning a new site

## Required Packages:
* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubunut:
```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install nginx git python3.6 python3.6-venv
```

## Nginx Virtual Host Config
* See nginx.template.conf
* Replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service
* See gunicorn-systemd.template.service
* Replace DOMAIN with, e.g., staging.my-domain.com

## Folder Structure:

Assume we have a user account at /home/username
/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc

