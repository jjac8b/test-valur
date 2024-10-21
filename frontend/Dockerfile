FROM node:18-alpine AS build

WORKDIR /app

ARG VUE_APP_API_BASE_URL
ENV VUE_APP_API_BASE_URL=${VUE_APP_API_BASE_URL}

COPY package*.json ./
RUN yarn install

COPY . .

RUN yarn run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
# Using ddefault 80 po
