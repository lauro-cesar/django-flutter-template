FROM nginx:1.19.0
RUN mkdir -p /etc/nginx/templates
COPY templates /etc/nginx/templates/
COPY nginx.conf /etc/nginx/
COPY etc/letsencrypt /etc/letsencrypt/