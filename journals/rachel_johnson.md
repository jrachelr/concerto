docker volume create pg-admin
docker volume create postgres-data
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build
docker compose up

to rebuild and make migrations
docker compose down
docker system prune
[delete docker volumes]
docker volume create pg-admin
docker volume create postgres-data
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build (for m1 users)
[in concerts api container CLI] python -m migrations up
[in users api container CLI] python -m migrations up

### 16 November

- list concerts
- create concert
- get single concert

### 17 November

- update concert
- delete concert
- updated readme with MVP, third party API endpoints

### 18 November

- pair programmed with Nikko refactoring concerts requests with user info as these requests are for favourite concerts
- brianstormed authentication process to allow only authenticated users to view their list of fovourite concert
  -pair programmed with Nikko refactoring concerts requests with user info as these requests are for favourite concerts
  -brianstormed authentication process to allow only authenticated users to view their list of fovourite concert

### 21 November

- researched Spotify API docs, attempted to build player with iframe API. Couldn't get it to work. Looked at Spotify dev community forum and it only works with podcasts.
- tested out regular spotify embedder, it's possible to dynamically update the embedder code with the Spotify url retrieved from ticketmaster API response. Can slice the artist id out and insert into the embedded player.
- Using embedder for now
  -researched Spotify API docs, attempted to build player with iframe API. Couldn't get it to work. Looked at Spotify dev community forum and it only works with podcasts.
  -tested out regular spotify embedder, it's possible to dynamically update the embedder code with the Spotify url retrieved from ticketmaster API response. Can slice the artist id out and insert into the embedded player.
  -Using embedder for now

### 22 November

- added localhost 8000 to cors allowed origins
- starting building front-end. attempting to start with login. installed tailwind and not working.

### 23 November

- fixed tailwind, was installed in project directory, not ghi. Login function still not working, log reads useNav cannot be used outside of browser router

### 28 November

- pair programmed with Nikko, got login wokring! had to remove await from promise function. starting logout

### 29 November

- logout appears to be functioning. We updated cors allowed hosts in users api and it's causing infinite loop of errors of 404 not found and 401 unauthorised
- login appears to still be functioning with the errors. starting signup page.
- signup page working! Jim sent a temp fix for 404 problem

### 30 November

- merged with group, so have synced code to debug issues.
- login, logout and signup working

### 30 November

-did sign up and logout

- continue building front-end.

### 1 December

- adding bg image
- wokring on auth on front end still. fixed issue with tempalte data - was access_token not token. managed to get the token in the front end after login, and clear after logout. signup looks like it's posting a new user, but the funciton isn't passing through to login correctly.

### 2 Decmeber

- fixed signup to login issue - had to update login funciton in auth to pass in email and password instead of username.
- felt super sick and feverish so slept most of the day :(
- login, logout and signup now working correctly and header / sidebar

### 5 December

- created skeleton of user favorites page. got it working but needs styling and addition of remove from favorite button.

### 6 December

- added remove favorite button. adding user info to page
- starting tests
