# this was sample script from lecture 


from mrjob.job import MRJob
from mrjob.step import MRStep

Class RatingsBreakdown(MRJob):
  def steps(self):
    return [MRStep(mapper = self.Mapper_get_ratings,
                   reducer = self.Reduce_count_ratings)
           ]
  def Mapper_get_ratings(self,_,line):
    (userID,MovieID,ratings,timestamp) = line.split('/t')
    yield MovieID,1
  
  def Reduce_count_ratings(self,key,values):
    yield key, sum(values)
if __name__ == '__main__':
  RatingsBreakdown.run()
