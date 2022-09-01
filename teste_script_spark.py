from pyspark.sql import SparkSession

sc = SparkSession.builder.appName('helloworld').getOrCreate()


print(type(sc), "/n")
print(dir(sc))