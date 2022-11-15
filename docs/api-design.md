### Log in

- Endpoint path: /token
- Endpoint method: POST

- Request shape (form):

  - username: string
  - password: string

- Response: Account information and a token
- Response shape (JSON):
  ```json
  {
    "account": {
      «key»: type»,
    },
    "token": string
  }
  ```

### Log out

- Endpoint path: /token
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Response: Always true
- Response shape (JSON):
  ```json
  true
  ```

<!-- /discovery/v2/events (TICKETMASTER API) -->

### Sign up

- Endpoint path: /signup
- Endpoint method: POST

- Request shape (form):

  - username: string
  - password: string

- Response: Account information and a token
- Response shape (JSON):
  ```json
  {
    "account": {
      «key»: type»,
    },
    "token": string
  }
  ```

### List of Concerts After Search

- Endpoint path: /concerts?location={USERINPUT}

- Endpoint method: «HTTP method»= GET
- Query parameters:

  - classificationName: = music (find music events)
  - city: = city name (filter by city)
  - preferredCountry: "us" (filter within the US)
  - apiKey:

- Headers:
<!--
  - Authorization: Bearer token -->

<!-- - Request shape (JSON):

  ```json
  «JSON-looking thing that has the
  keys and types in it»
  ``` -->

- Response: List of concerts in your area

- Response shape (JSON):

{ concerts:
{
name: str
price: int
dates: date
venue: str
}
}

<!-- "embedded": {
"events": [
"priceRanges"
-> "min", "max"
{
"dates" : {
"localDate",

"embedded"
"venues" -> "name"

"attractions"
"name"
"image"
"external links"

    }
        }
    ] -->

### Favorite Concert

- Endpoint path: /favorites/user/{USERID}
- Endpoint method: GET

- Response: Get favorite concerts

- Response shape (JSON):
  { favorites: {
  concert_id: int
  name: str
  price: int
  dates: date
  venue: str
  }
  }

```

```

#

### Favorite Concert

- Endpoint path: /favorites/user/{USERID}
- Endpoint method: POST

- Request shape (JSON):
  {
  concert_id: int
  user_id: int
  }

- Response: Add Favorite

- Response shape (JSON):
  {
  concert_id: {
  name:
  venue:
  dates:
  price:
  }
  user_id: int
  }

```

```

### Favorite Concert

- Endpoint path: /favorites/user/{USERID}/{CONCERTID}
- Endpoint method: DELETE

- Request shape (JSON):

- Response: Remove concert from favorites
- Response shape (JSON):
  {"message": Your concert has been deleted!}

```

```

#4 crud methods for users and favorites

#Favorites - Create, Read, Delete
#Users - Create, Update, Read, Delete
(JWT Library)

#
