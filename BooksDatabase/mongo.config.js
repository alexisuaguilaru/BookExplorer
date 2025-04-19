db = db.getSiblingDB(process.env.DATABASE);

db.createUser({
  user: process.env.MONGO_WRITE_USERNAME,
  pwd: process.env.MONGO_WRITE_PASSWORD,
  roles: [
    { role: "readWrite", db: process.env.DATABASE },
  ]
});

db.createUser({
  user: process.env.MONGO_READ_USERNAME,
  pwd: process.env.MONGO_READ_PASSWORD,
  roles: [
    { role: "read", db: process.env.DATABASE },
  ]
});