# Data models

## Users Microservice

---

### Users

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| first_name       | string | no     | no       |
| last_name        | string | no     | no       |
| email            | string | no     | no       |
| password         | string | no     | no       |
| username         | string | yes    | no       |
| id               | int    | yes    | no       |
| hashed_password  | string | yes    | no       |


## Concerts Microservice

---

### Concerts

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| user_id          | int    | yes    | no       |
| concert_id       | int    | yes    | no       |
| city             | string | yes    | no       |
| state            | string | yes    | no       |
| concert_name     | string | yes    | no       |
| artist_name      | string | yes    | no       |
| start_date       | string | yes    | no       |
| max_price        | int    | yes    | no       |
| min_price        | int    | yes    | no       |
| spotify_url      | int    | yes    | no       |
| image_url        | string | yes    | no       |
| favorite         | bool   | yes    | no       |
