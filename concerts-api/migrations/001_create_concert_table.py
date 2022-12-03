steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE favorite_concerts (
            id SERIAL PRIMARY KEY NOT NULL,
            concert_name VARCHAR(1000) NOT NULL,
            artist_name VARCHAR(1000) NOT NULL,
            start_date DATE NOT NULL,
            min_price INTEGER NOT NULL,
            max_price INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            spotify_url VARCHAR(1000) NOT NULL,
            image_url VARCHAR(1000) NOT NULL,
            favorite BOOLEAN NOT NULL DEFAULT false
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE favorite_concerts;
        """
    ],
]
