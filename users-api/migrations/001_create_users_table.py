steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE user_info (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(1000) NOT NULL,
            last_name VARCHAR(1000) NOT NULL,
            email VARCHAR(1000) NOT NULL UNIQUE,
            hashed_password VARCHAR(200) NOT NULL,
            username VARCHAR(1000) NOT NULL UNIQUE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE user_info;
        """
    ],
]
