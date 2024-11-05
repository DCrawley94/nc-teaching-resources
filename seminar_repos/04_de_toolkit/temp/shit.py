

def listin(s3):
    objects = s3.list_buckets()
    print(objects)
