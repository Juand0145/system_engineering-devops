# 0x16. API advanced
In this directory, we will find a compilation of files that will help us to understand the concept of using API to read write and understand information in Json information and help us answer the next questions?
-   How to read API documentation to find the endpoints you’re looking for
-   How to use an API with pagination
-   How to parse JSON results from an API
-   How to make a recursive API call
-   How to sort a dictionary by value
## Files
 - 0-subs.py is a unction that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA "Reddit API") and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
 - 1-top_ten.py is a a function that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA "Reddit API") and prints the titles of the first 10 hot posts listed for a given subreddit.
 - 2-recurse.py is a _recursive function_ that queries the [Reddit API](https://intranet.hbtn.io/rltoken/odMvR9obKnQCx5EaM6_YFA "Reddit API") and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
