import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in file_handle:
    print(line.decode().strip())