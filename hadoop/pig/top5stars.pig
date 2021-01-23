--this was sample script from  course: [The Ultimate Hands on Hadoop](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/)

--Goal: find the oldest 5 Stars movie
--dataset: from movielens

--1.  create relation named ratings

ratings = LOAD '/user/maria_dev/ml_100k/u.data' AS
(userID:int, movieID:int, ratingTime: int);

/*2. PigStorage; if you need different delimeter of pipe characters
# PigStorage: The PigStorage() function loads and stores data as structured text files. 
It takes a delimiter using which each entity of a tuple is separated as a parameter. By default, it takes '\t' as a parameter./*

