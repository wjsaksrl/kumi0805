import io
f = open("myfile.txt", "r", encoding="utf-8")
f = io.StringIO("some initial text data")
print(f)