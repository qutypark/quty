# this was sample script from  course: [The Ultimate Hands on Hadoop](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/)
# Goal: sort the movies by their numbers of raitings
# strategy1. Map to key,values pair(MovieID,1)
# strategy2. Reduce with output of raiting count, movie id
# strategy1. send to second reducer to sort by rating count


# edit: nano TopMovie.py
# execute: python TopMovie.py u.data

from mrjob.job import MRJob
from mrjob.step import MRStep

Class TopMovie(MRJob):
  def steps(self):
    # can chain map/reduce stages together
    return [MRStep(mapper = self.mapper_get_ratings,
                   reducer = self.reducer_count_ratings),
            MRStep(reducer = self.reducer_sorted_output) #second reducer
           ]
  def mapper_get_ratings(self,_,line):
    (userID,MovieID,ratings,timestamp) = line.split('/t')
    yield MovieID,1
  
  def reducer_count_ratings(self,key,values):
    yield str(sum(values)).zfill(5),key #make string into 5 digit num
   
  def reducer_sorted_output(self,count,movies):
    for movie in movies:
      yield movie,count
  
if __name__ == '__main__':
  TopMovie.run()
