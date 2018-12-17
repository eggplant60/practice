# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.test

#co = db.aggregate
# co.insert({'名前':'一郎', '性別':'男', '国語':80, '数学':60})
# co.insert({'名前':'二郎', '性別':'男', '国語':50, '数学':70})
# co.insert({'名前':'三郎', '性別':'男', '国語':60, '数学':90})
# co.insert({'名前':'花子', '性別':'女', '国語':70, '数学':70})
# co.insert({'名前':'洋子', '性別':'女', '国語':60, '数学':80})
# print(co.count())

#co_join = db.join
# co_join.insert({'ID': 1, '性別':'男'})
# co_join.insert({'ID': 2, '性別':'女'})
# print(co_join.count())

co_orders = db.orders
co_orders.drop()
co_orders.insert([
    { "_id" : 1, "item" : "almonds", "price" : 12, "quantity" : 2 },
    { "_id" : 2, "item" : "pecans", "price" : 20, "quantity" : 1 },
    { "_id" : 3  }
])
print(co_orders.count())

co_inventory = db.inventory
co_inventory.drop()
co_inventory.insert([
    { "_id" : 1, "sku" : "almonds", "description": "product 1", "instock" : 120 },
    { "_id" : 2, "sku" : "bread", "description": "product 2", "instock" : 80 },
    { "_id" : 3, "sku" : "cashews", "description": "product 3", "instock" : 60 },
    { "_id" : 4, "sku" : "pecans", "description": "product 4", "instock" : 70 },
    { "_id" : 5, "sku": None, "description": "Incomplete" },
    { "_id" : 6 },
    { "_id" : 7, "sku" : "almonds", "description": "product 7", "instock" : 150 },
])
print(co_inventory.count())


"""
https://docs.mongodb.com/manual/aggregation/

{$group: {'_id': key, <field1(任意)>: { <accumulator1> : <expression1> }, ... }}   -> keyごとの集計
{$match: { <query> }}              ->  find と同じだが他のパイプラインに繋げられる

accumulator の種類
$addToSet
$avg
$first
$last
$max
$mergeObjects
$min
$push
$stdDevPop
$stdDevSamp
$sum

"""

"""
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       as: <output array field>
     }
}

{ $unwind: <field path> }
"""

# pipe = [
#     # {'$match': { '名前': {'$ne': '三郎'}}},             # 三郎を除外
#     # {'$group': {'_id': '$性別', 'count': {'$sum': 1}}}, # 男女別の合計
#     # { '$group' : { '_id': '$性別', 'average': { '$avg': '$国語'}}} # 男女別の国語の平均
#     # { '$group' : { '_id': 'null', 'total': { '$sum': '$数学'}}} # 総合計
#     # {'$lookup': {'from': 'co',
#     #              'localField': '性別',
#     #              'foreignField': '性別',
#     #              'as': 'new'}     # 新しいフィールド名
#     # },
#     #{'$unwind': '$new'}
# ]
# agg = co_join.aggregate(pipeline=pipe)


agg = db.orders.aggregate(
    [
        {
            '$lookup':
            {
                'from': "inventory",
                'localField': "item",
                'foreignField': "sku",
                'as': "inventory_docs"
            }
        },
        {'$unwind': '$inventory_docs'}
    ]
)

pprint(list(agg))
