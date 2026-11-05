book = {
    "name" : "samphony mordegan" ,
    "writer" : "abas marofy" ,
    "print day" : 2001 ,
    "language" : ["farsi"]
}
book["language"] = ["farsi" , "english" , "german"]
book["price"] = 1000000
book["publisher"] = "hashem"
del book["publisher"]
if (book["print day"] < 2005):
    print("old")
else:
    print("new")
print(book)
for key in book :
    print(key)
    print(book[key])
