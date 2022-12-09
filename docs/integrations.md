The concerts microservice uses the ticketmaster API to show a list view of concerts.
For the purposes of Concerto, a request to ticketmaster API contains a location key and event type key.

This is an example request searching for music events in Los Angeles:

https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=324&apikey=btsaKZ8FElrG6RkY7eRLIRvqVfJ9P374

The ticketmaster get request returns a JSON object as detailed below:

![Ticketmaster JSON response structure](readme_images/tm_response.png)

In addition to pulling data from the ticketmaster API, Concerto also embeds a Spotify player into the browser. The data is passed from the ticketmaster response into the Spotify API request. Using the artist name, the embedded Spotify player will be populated with songs from that artist.

The data flow from Ticketmaster to Spotify is detailed below:

![Data flow from Ticketmaster to Spotify](readme_images/tm_spotify_dataflow.png)
