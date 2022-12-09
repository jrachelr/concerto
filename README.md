# Concerto

## Group 4 Members
- Esteban Chirinos
- Rachel Johnson
- Nicolette Mabeza
- Jimmy Nguyen

## Functionality
- Visitors to the site can search for local entertainment based off whatever location/destination as they please.

- Users who are signed in will have the ability to favorite such concerts to add to a list of "Favorited Concerts"

- In addition to searching for concerts, users will be able to sample such artists music directly from the application with the Spotify Embedded player.


## Design
Concerto is a full-stack web application for music lovers to search for concerts. It removes the friction between searching for concerts and moving to another application to sample music by an artist, by embedding a Spotify player within the browser window.

- [API design](docs/api-design.md)
- [Data Model](docs/data-model.md)
- [GHI](docs/ghi.md)
- [Integrations](docs/integrations.md)

## Getting started

- Fork repository

- Clone the repository to your local machine

- Get ticketmaster API key https://developer.ticketmaster.com/products-and-docs/apis/getting-started/

- Get google autocomplete API key https://developers.google.com/maps/documentation/places/web-service/autocomplete

- cd into the new project directory

- Run `docker volume create pg-admin`

- Run `docker volume create postgres-data`

- Run `docker compose build`

- Run `docker compose up`

- Make .env file and place the 2 API keys in there (THIS IS FOR LOCAL TESTING)
