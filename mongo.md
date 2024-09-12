## MONGODB DOCKER

```bash
docker pull mongo
```

'''

```bash
docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongo -e MONGO_INITDB_ROOT_PASSWORD=strong_password mongo
```

Install Mongodb for vscode extension
Hit connect: "mongodb://username:password@localhost:27017/database?authSource=admin"

Now you can install mongosh 'brew install mongosh' and launch mongoshell by rightclicking on the connection.
or open mongodb compass and enter the above connection string.

```
show dbs
use school
db.createCollection("students")
db.students.insertOne({name:"ajay",age:23,gpa:3.4})
db.students.insertMany([{name:"akash",age:12,gpa:1.4}, {name:"parth",age:17,gpa:2.4}])

## find
db.students.find()
db.students.find().sort({name:1})
db.students.find().sort({name:-1})
db.students.find().sort({name:1}).limit(1)
db.students.find({name:"ajay"})
db.students.find({name:"ajay",gpa:2},{_id:false,name:true}) #returns only name of the people with name ajay and gpa:2

## Update
db.students.updateOne({name:"ajay"},{$set:{fulltime:false}})
db.students.updateMany({},{$set:{fulltime:false}})
db.students.updateMany({name:"ajay"},{$unset:{fulltime:""}})
db.students.updateMany({fulltime:{$exists:false}},{$set:{fulltime:true}}) #anyone without fulltime will be added with fulltime true field

# Delete
db.students.deleteOne({name:"akash"})
db.students.deleteMany({gpa:{$exists:true}})

## Comparision Operators
db.students.find({name:{$ne:"ajay"}}) #not equal
db.students.find({age:{$lte:27}})  #less than or equal to
db.students.find({age:{$lte:20}})  #less than
db.students.find({gpa:{$gte:2.7}}) #greater than or equal to
db.studetns.find({name:{$in:["ajay","parth"]}}) #in
db.students.find({name:{$nin:["ajay","parth"]}}) #not in

## Logical Operators
db.students.find({$and:[{age:{$lt:20}},{name:{$in:["spongebob","akash","ajay"]}}]})
db.students.find({$or:[{age:{$lt:20}},{name:{$in:["spongebob","akash","ajay"]}}]})
db.students.find({age:{$not:{$gte:20}}})

## Indexes
db.students.find({name:"ajay"}).explain("executionStats") #documents examined 5
db.students.createIndex({name:1}) #sorts contents of index in ascending is name:1 and descening if -1
db.students.find({name:"ajay"}).explain("executionStats") # documents examined 1
db.students.getIndexes()
db.students.dropIndex("name_1")
db.students.getIndexes()

db.students.drop()
show collections
```
