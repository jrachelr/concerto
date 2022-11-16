steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE concerts (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(1000) NOT NULL,
            artist VARCHAR(1000) NOT NULL,
            date DATE NOT NULL,
            min_price INTEGER NOT NULL,
            max_price INTEGER NOT NULL,
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE concerts;
        """
    ]
]
