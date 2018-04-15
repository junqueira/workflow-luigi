#!/bin/sh

rm hello.txt world.txt

# https://s3-us-west-2.amazonaws.com/pycon-2017-luigi-presentation-data/credentials.txt

#sudo lsof -t -i tcp:8082 | xargs kill -9
#luigid --background --logdir=./logs --port=8082

#python hello_world.py SomeTask
#python hello_word.py HelloTask
#python hello_world.py WorldTask

#python hello_world.py HelloWorldTask --workers=2

#python hello_world.py HelloWorldTask --id='test'

export LUIGI_CONFIG_PATH=staging.luigi.cfg

# credentials in aws config file
#python data_pipeline.py AllData --id='123'

