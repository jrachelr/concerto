11/16/22

- Created Dockerfile.dev for concerts-api and updated docker-compose.yml to include concerts, pg-admin, and postgres services
- Pair programmed with teammates to create routers and queries for concerts (get and post)

11/17/22

- Finished routers for concerts
- Added get request for Ticketmaster API
  -- Created function that manipulated the data we get into the same shape as our favorite concerts model

11/18/22

- Refactored concerts endpoints to include user_id
- Added user_id to favorite_concerts table
- Reviewed authentication and figured out which endpoints should require a user to be authenticated

11/21/22

- Created basic search bar component
- Used Google Places AutoComplete to enable autocomplete functionality within search bar component
- Incorporated Google Geocoding API to get latlong from search bar input

11/22/22

- Fixed Ticketmaster API request so that it would take in city and state instead of lat and long
- Fixed CSS of search bar component

11/23/22

- Fixed authentication issues

11/28/22

- Started Concerts list component

11/29/22

- Able to use search component to get latitude and longitude and then get concerts based on that data

11/30/22

- Pair programmed to fix authentication and tested it to make sure it works for concerts and user

12/1/2

- Fixed token issue and now able to get token on the front end and use it with other components
  -- Had to change variable name from "token" to "access_token"
- Fixed signup issue and now able to get token on frontend when user signs up
- Fixed login issue
  -- username was being passed into login function instead of email

12/2/22

- Completed Concert List component which gives a list of concerts based on search criteria
- Created favorite button functionality
- Created concert drawer to show concert details
- Created Music Player component to display spotify embedded music player for artist in concert details

12/5/22

- Started load more concerts functionality
  -- Having issues where the concert state did not clear for a new search so the list of concerts was being added to a previous searches results

12/6/22

- Completed load more concerts functionality
  -- Created a useEffect that triggered the GetConcerts fn when state of page changes

12/7/22

- Fixed 401 error showing up on console before user tried logging in
- Fixed Favorite Concerts error showing null ID
  -- Separating fetches for user and token in two UseEffects
