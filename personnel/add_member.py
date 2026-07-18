# =====================================================
#  personnel/add_member.py — คนรับผิดชอบ: ______________________
#  หน้าที่: รับข้อมูลลูกน้องใหม่ สร้างเป็น dict แล้วเพิ่มเข้าลิสต์แฟมิลี่
# =====================================================
from data import family_members

def add_member(name, age, power, money):
    
    if power >= 8 :
        role = "Hitman"
    else:
        role = "Slave"

    if money >= 1000000 :
        role = "Sponsor"
    else:
        role = "Slave"
    new_people = {
        "name" : name ,
        "age" : age ,
        "role" : role ,
        "power" : power ,
        "money" : money ,
        "equiment" : "ไม่มี"
    }
    family_members.append(add_member)
    return

# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.add_member
if __name__ == "__main__":
    add_member("Vito", 20, 9, 500)
    print(family_members)   # ต้องเห็น Vito ต่อท้ายลิสต์ และ role เป็น Hitman
