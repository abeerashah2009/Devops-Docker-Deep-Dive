# Use a maintained Node.js image
FROM node:22-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies first
COPY package*.json ./
RUN npm install

# Copy application source
COPY . .

# Expose app port
EXPOSE 8080

# Start the app
CMD [ "node", "app.js" ]
