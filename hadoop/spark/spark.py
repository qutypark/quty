# pip install library below in advance
import findspark
from pyspark import SparkContext

import os

os.environ["SPARK_HOME"] = "C:local/spark"
findspark.init()
