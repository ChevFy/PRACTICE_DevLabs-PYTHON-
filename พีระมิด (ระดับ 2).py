
n = int(input())

for i in range(n) :
    print( " " * (n-i-1) + "*" * (1+(i)*2) )

import json

def readjson():
        # ข้อมูล JSON ที่เราต้องการอ่าน
        x = '{ "name":"John", "age":30, "city":"New York"}'
        # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
        y = json.loads(x)
        # ทำการเรียกข้อมูล age ออกมาแสดง
        print(y["city"])

readjson()