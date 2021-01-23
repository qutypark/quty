--this was sample script from  course: [The Ultimate Hands on Hadoop](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/)

--Goal: find the oldest 5 Stars movie
--dataset: from movielens
-- u.data, u.item: files installed on HDFS

--1.  create relation named "ratings"

ratings = LOAD '/user/maria_dev/ml_100k/u.data' AS
(userID:int, movieID:int, ratingTime: int);

--2. PigStorage; since releaseDate has delimeter pipe character

metadata = LOAD '/user/maria_dev/ml_100k/u.item' USING PigStorage('|') AS
(movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelase:chararray, imbdlink: chararray);

--3. creating a relation from another relation; FOREACH, GENERATE

nameLookup = FOREACH metadata GENERATE movieID,moveTitle, 
ToUnixTime(ToDate(releaseDate,'dd-MMM-yyyy')) AS releaseTime;

--4. figure out all the ratings associated with each individual movie by 'GroupBy'
-- create a BAG in pig that contains tuples of all the individual rows associated with a given movieID
-- # similar to reducer but don't have to create reducer! 

ratingsByMovie = GROUP raitings BY movieID;
DUMP ratingsByMovie;
 
--5. get average of ratings

avgRatings = FOREACH raitingsByMovie GENERATE group as movieID,
AVG(ratings.raitng) AS avgRating;

-- *group: ratingsByMovie was created by GroupBY

--6. filter over 4star(to get 5stars)

fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;

--7. join it with moviename by movieID

fiveStarswithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;
DUMP fiveStarswithData;

--8. get oldest movie <- order

oldestFiveStarMovies = ORDER fiveStarswithDATA BY nameLookup::releaseTime;
DUMP oldestFiveStarMovies;

