FROM node
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:stable-alpine3.20-perl
COPY --from=0 /usr/src/app/dist /usr/share/nginx/html
EXPOSE 8080
CMD [ "nginx", "-g", "daemon off;"]