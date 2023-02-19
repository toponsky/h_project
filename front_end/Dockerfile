### STAGE 1: Build ###
FROM node:12.14-alpine AS build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build:prod



### STAGE 2: Run ###
FROM nginx:1.17.1-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf