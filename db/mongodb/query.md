#### 查询数据的语法格式
db.collection.find(query, projection)
db.collection.find(query, {title: 1, by: 1}) // inclusion模式 指定返回的键，不返回其他键
db.collection.find(query, {title: 0, by: 0}) // exclusion模式 指定不返回的键,返回其他键

#### 两种模式不可混用
db.collection.find(query, {title: 1, by: 0})
