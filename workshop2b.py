name = str(input("ชื่อ : "))
age = int(input("อายุ : "))
height = int(input("ส่วนสูง : "))
power = int(input("พละกำลัง : "))
money = int(input("เงินติดตัว : "))

if power == 3 or power == 4:
    print ("ผ่าน : เด็กน้อย")
elif power == 5 or power == 6:
    print ("ผ่าน : เด็กเดิน")
elif power == 7 or power == 8:
    print ("ผ่าน : มือขวา")
elif power == 9 or power == 10:
    print ("ผ่าน : เป็นหัวแถว")
else :
    print ("ไม่ผ่าน")