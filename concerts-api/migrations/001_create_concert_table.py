steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE concert_info (
            id SERIAL PRIMARY KEY NOT NULL,
            concert_name VARCHAR(1000) NOT NULL,
            artist_name VARCHAR(1000) NOT NULL,
            start_date DATE NOT NULL,
            min_price INTEGER NOT NULL,
            max_price INTEGER NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE concert_info;
        """
    ],
]
