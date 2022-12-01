docker volume create pg-admin
docker volume create postgres-data
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build
docker compose up

### 16 November
-list concerts
-create concert
-get single concert

### 17 November
-update concert
-delete concert
-updated readme with MVP, third party API endpoints

### 18 November
-pair programmed with Nikko refactoring concerts requests with user info as these requests are for favourite concerts
-brianstormed authentication process to allow only authenticated users to view their list of fovourite concert

### 21 November
-researched Spotify API docs, attempted to build player with iframe API. Couldn't get it to work. Looked at Spotify dev community forum and it only works with podcasts.
-tested out regular spotify embedder, it's possible to dynamically update the embedder code with the Spotify url retrieved from ticketmaster API response. Can slice the artist id out and insert into the embedded player.
-Using embedder for now

### 22 November
-added localhost 8000 to cors allowed origins
- starting building front-end. attempting to start with login. installed tailwind and not working.

### 30 November
-did sign up and logout
- continue building front-end.
