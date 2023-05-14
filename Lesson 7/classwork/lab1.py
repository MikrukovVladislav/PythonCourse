#
#  БД "Система проверки задач"
# Описание предметной области. БД создается для информационного обслуживания учебного процесса.
# Преподаватель каждый урок выдает некоторое количество задач в качестве домашнего задания.
# Каждый ученик решает задачи и переводит ее в статус решенную выкладывая ее на Git
# Система, забирает задачу с Git'а и проверяет каждую задачу прогоняя ее через тесты и запуская ее в виртульном окружении
# и либо подтверждает ее статус как решенную либо возвращает сообщение об ошибки ( меняя ее статус как не решенную.)
#
#
# Разработайте систему с учетом бизнес сущностей:
# Группа, Преподаватель, Студент, Занятие, Задача
#
# Запросы:
# 1. Выдавать список задач по категории (категориями являются темы занятий)
# 2. Выдавать список задач по уровню сложности
# 3. Выдавать список решенных и не решенных задач для слушателя
# 4. Выдавать весь список задач выданный слушателю
# 5. Выдавать список группы по преподавателю
# 6. Предусмотреть возможность изменения статуса задачи для конкретного слушателя
# 7. Выдавать процент решенных задач. (Соотношение между общим кол-вом и решенным)
# 8. Выдавать процент успеваемости по всей группе.
#
# Система:
# 1. Написать утилиту которая генерирует файлы taskN.py в папке classwork по номеру задачи.
# Задачи все храняться в БД.


from getpass import getpass
from mysql.connector import connect, Error

#Link: https://editor.ponyorm.com/user/kamakado/lesson7_classwork/mysql
#123
sql = ["SELECT * FROM task WHERE id_category=(SELECT id FROM category WHERE name=\"testCategory1\")",
       "SELECT * FROM task WHERE id_difficult=(SELECT id FROM difficult WHERE name=\"easy\")",
       "SELECT * FROM task WHERE id IN (SELECT tasks FROM task_student WHERE students=(SELECT id FROM student WHERE name=\"Fu Jiehong\") AND status IN (SELECT id FROM status WHERE name IN (\"run\", \"finish\")))",
       "SELECT * FROM task WHERE id IN (SELECT tasks FROM task_student WHERE students=(SELECT id FROM student WHERE name=\"Fu Jiehong\"))",
       "SELECT name from student WHERE id IN (SELECT students FROM teacher_students WHERE teachers=(SELECT id FROM teacher WHERE name=\"Kelly Murphy\"))",
       "",
       "SELECT status, count(*) * 100.0 / (select count(*) FROM task_student) FROM task_student WHERE task_student.status=3",
       "SELECT status, count(*) * 100.0 / (select count(*) FROM task_student WHERE students IN (SELECT students FROM teacher_students WHERE teachers=2)) FROM task_student WHERE task_student.status=3 AND students IN (SELECT students FROM teacher_students WHERE teachers=2);"]

try:
    with connect(
        host="mikrukov.vladislav.fvds.ru",
        user="course",
        password="Course123!@#",
        database="PythonCoursesLesson7",
    ) as connection:
        for sql_request in sql:
            prnt_msg = "sql_request = " + sql_request
            i = 0
            tmpStr = ""
            while i < len(prnt_msg):
                tmpStr += "*"
                i += 1
            print("******" + tmpStr + "******")
            print("***** " + prnt_msg + " *****")
            with connection.cursor() as cursor:
                print("bepp")
                cursor.execute(sql_request)
                result = cursor.fetchall()
                print("result = " + str(result))
                for row in result:
                    print(row)

            print("******" + tmpStr + "******")
except Error as e:
    print(e)