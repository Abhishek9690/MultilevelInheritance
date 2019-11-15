class android:
    def android(self):
        print("android...")
class abhishek(android):
    def java(self):
        print("java...")
class Oracle(abhishek):
    def dbms(self):
        print("sql...")

obj=Oracle()
obj.dbms()
obj.java()
obj.android()
