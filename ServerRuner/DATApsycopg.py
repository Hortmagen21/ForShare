import psycopg2
testbase=psycopg2.connect("dbname=d7f6m0it9u59pk user=iffjnrmpbopayf host=ec2-54-83-1-101.compute-1.amazonaws.com password=20d31f747b4397c839a05d6d70d2decd02b23a689d86773a84d8dcfa23428946 port=5432")
curser=testbase.cursor()
#curser.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#curser.execute("INSERT INTO fortest (name,id) VALUES(%s, %s)",("alex",14))
curser.execute("SELECT * FROM acctester")
for row in curser.fetchall():
    print(row)
    print(row[0])
    print(type(row[0]))


#curser.execute("SELECT * FROM test;")
#curser.fetchone()
#("a",101)
testbase.commit()
curser.close()
testbase.close()
