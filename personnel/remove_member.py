# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: Phumiphat
#  หน้าที่: ลบลูกน้องออกจากแฟมิลี่ตามชื่อ
# =====================================================
from data import family_members

def remove_member(target_name):
#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False
    for members_remove in family_members :
        if members_remove["name"].lower() == target_name.lower() :
            family_members.remove(members_remove)
            return True
    return False
    


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("Luigi"))   # ครั้งแรกต้องได้ True
    print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
