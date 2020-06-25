
import mysql_object

def write_db():
    person = mysql_object.create_connection()
    obj = mysql_object.PerSon(id=123345, name= "Kien Nguyen Ngoc")
    person.add(obj)
    try:
        person.commit()
    except Exception:
        person.rollback()

    person.close()
    return person

if __name__ == "__main__":
    write_db()