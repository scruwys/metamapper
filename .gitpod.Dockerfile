FROM getmetamapper/metamapper:latest as metamapper

FROM gitpod/workspace-postgres

ENV METAMAPPER_DB_HOST localhost
ENV METAMAPPER_FERNET_KEY 'mHYPeDvFJ1LtDClYGtckO-PZCBZfM2xLpWKqu7qQSkI='
ENV METAMAPPER_SECRET_KEY 'f+4j@p$=%+3h^*e0hhobo0g+0smb)v&1ypg$q7vdxgd9b3sj%4'

COPY --from=metamapper /usr/local/metamapper /usr/local/metamapper/
