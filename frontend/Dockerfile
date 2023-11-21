FROM node:21-alpine

WORKDIR /get-by/frontend/

COPY package*.json /get-by/frontend/
RUN npm install

COPY . /get-by/frontend/

CMD ["npm", "start"]