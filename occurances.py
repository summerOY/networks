import jieba
import time

start = time.perf_counter()
txt = open("./book.txt", "r", encoding="utf-8").read()
excludes = {"二人","只见", "一个","只是","看时","不敢","一面","不得","次日","不曾","如何", "来到","且说","不知","不是", "人马", "你们", "我们", "好汉", "军马", "这个", "今日", "妇人", "先锋", "知府", "什么", "说道", "他们", "那里","银子", "梁山", "两个","众人","这里","兄弟","出来", "梁山泊","小人","便是","问道","起来","甚么","因此","却是","正是","三个","如此"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "哥哥":
        word = "宋江"
    elif word == "宋江道":
        word = "宋江"
    elif word == "头领":
        word = "林冲"
    elif word == "鲁达":
        word = "鲁智深"
    elif word == "呼延":
        word = "呼延灼"
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
dur = time.perf_counter() - start
print("running time: {:.2f}s".format(dur))
print("-----------------------------")
