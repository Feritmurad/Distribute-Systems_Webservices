# Distribute Systems - Webservices
First practical assignment of the Distributed Systems course.
# TODO
GET /movies?limit=x : Returns the first x popular movies.
GET /movies/similar_genres?movie=<name> : Returns the movies that have exactly the same genres as the movie with the given id.
GET /movies/similar_runtime?movie=<name> : Returns the movies that have a similar runtime (maximum of 10 minutes difference) as the movie with the given id.
GET /movies/overlapping_actors?movie=<name> : Returns the movies that have two overlapping actors (the first 2 actors listed) as the movie with the given id.
GET /movies/average_score : Takes a list of movie ids in the request body and returns a barplot comparing their average scores.
DELETE /movies/<name> : Deletes the movie with the given id from the database.
GET /movies/likes : Returns liked movies.
POST /movies/likes?movie=<name> : Adds a like to the movie with the given name.
DELETE /movies/likes?movie=<name> : Removes a like from the movie with the given name.

# TODO 
Errors in api