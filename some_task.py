import luigi


class s3File(luigi.Config): #Class matches .cfg section
	bucket = luigi.Parameter()
	key = luigi.Parameter()

class SomeTask(luigi.Task):
	def output(self):
		return luigi.contrib.s3.S3Target(
			path='s3://{}/{}'.format(
				s3File().bucket, s3File.key()
			)
		)