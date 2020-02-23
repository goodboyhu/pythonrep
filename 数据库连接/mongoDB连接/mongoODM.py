from mongoengine import connect,Document,EmbeddedDocument,StringField,IntField,FloatField,ListField,EmbeddedDocumentField

connect('student')

SEX_CHOICES=(('male','男'),('female','女'))

# 嵌套型文档
class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score=FloatField(required=True)
class Student(Document):
    name=StringField(max_length=32, required=True)
    age=IntField(required=True)
    sex = StringField(choices=SEX_CHOICES,required=True)
    school = StringField()
    grade=FloatField()
    address=StringField()
    grades=ListField(EmbeddedDocumentField(Grade))


class TestmongoODM(object):
    def add_one(self):
        yuwen=Grade(
            name='语文',
            score=90)
        shuxue = Grade(
            name='数学',
            score=100)
        stu_obj=Student(
            name='张三2',
            age=15,
            sex='male',
            grades=[yuwen,shuxue]
        )

        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_all(self):
        return Student.objects.all()

    def get_from_oid(self,oid):
        return Student.objects.filter(pk=oid).first()

    def update(self):
        # 修改一条
        rest = Student.objects.filter(sex='male').update_one(inc__age=100)
        # 修改多条，男生年龄都加10
        # rest = Student.objects.filter(sex='male').update(inc__age=10)
        return rest

    def delete(self):
        # 删除一条
        # rest = Student.objects.filter(sex='male').first().delete()
        # 删除多条
        rest = Student.objects.filter(sex='male').delete()



def main():
    obj=TestmongoODM()

    # rest=obj.add_one()
    # print(rest.pk)

    # rest=obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rest = obj.get_all()
    # for row in rest:
    #     print(row.name)

    # rest = obj.get_from_oid('5e527558ebaf5f2e2f8b8a08')
    # if rest:
    #     print(rest.id)
    #     print(rest.name)

    # rest = obj.update()
    # print(rest)

    rest = obj.delete()
    print(rest)




if __name__ == '__main__':
    main()
