import luigi
from time import sleep
import os


class SomeTask(luigi.Task):
	def run(self):
		# Code that does something
		pass

	def output(self):
		return [SomeTarget()]
		# Target implements an exists() method 
	
	def requires(self):
		return [AnotherTask()]


class MakeDirectory(luigi.Task):
	path = luigi.Parameter()  #significant=False	

	def output(self):
		return luigi.LocalTarget(self.path)

	def run(self):
		os.makedirs(self.path)


class HelloTask(luigi.Task):
	path = luigi.Parameter()

	def run(self):
		# sleep(60)
		# with open('hello.txt', 'w') as hello_file:
		with open(self.path, 'w') as hello_file:
			hello_file.write('Hello')
			hello_file.close()

	def requires(self):
		return [
			MakeDirectory(path=os.path.dirname(self.path)),
		]

	def output(self):
		# return luigi.LocalTarget('hello.txt')
		return luigi.LocalTarget(self.path)


class WorldTask(luigi.Task):
	path = luigi.Parameter()

	def run(self):
		# sleep(30)
		# with open('world.txt', 'w') as world_file:
		with open(self.path, 'w') as world_file:
			world_file.write('World')
			world_file.close()

	def requires(self):
		return [
			MakeDirectory(path=os.path.dirname(self.path)),
		]

	def output(self):
		# return luigi.LocalTarget('world.txt')
		return luigi.LocalTarget(self.path)
		

class HelloWorldTask(luigi.Task):
	id = luigi.Parameter(default='test')

	def run(self):
		# sleep(30)
		# with open('hello.txt', 'r') as hello_file:
		with open(self.input()[0].path, 'r') as hello_file:
			hello = hello_file.read()
		# with open('world.txt', 'r') as world_file:
		with open(self.input()[1].path, 'r') as world_file:
			world = world_file.read()
		# with open('hello_world.txt', 'w') as output_file:
		with open(self.output().path, 'w') as output_file:
			content = '{} {}!'.format(hello, world)
			output_file.write(content)
			output_file.close()
		
	def requires(self):
		return [
			HelloTask(path='results/{}/hello.txt'.format(self.id)), 
			WorldTask(path='results/{}/world.txt'.format(self.id)),
			PrintWordTask(path='results/{}/hello.txt'.format(self.id), word='Hello'),
			PrintWordTask(path='results/{}/world.txt'.format(self.id), word='World 123'),
		]

	def output(self):
		path = 'results/{}/hello_world.txt'.format(self.id)
		return luigi.LocalTarget(path)


class PrintWordTask(luigi.Task):
	path = luigi.Parameter()
	word = luigi.Parameter()

	def output(self):
		return luigi.LocalTarget(self.path)

	def run(self):
		with open(self.path, 'w') as out_file:
			out_file.write(self.word)
			out_file.close()


if __name__ == '__main__':
	luigi.run()