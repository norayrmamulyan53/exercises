from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name="անուն")
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name="Դասատու",
                                related_name='subject_teacher', blank=True, null=True)
    students = models.ManyToManyField('Student', blank=True)

    class Meta:
        verbose_name = 'Առարկա'
        verbose_name_plural = 'Առարկաներ'
        ordering = ['id']

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="Անուն, Ազգանուն")
    age = models.IntegerField(default=6, verbose_name="Տարիք")
    join_date = models.DateTimeField(auto_now_add=True, verbose_name="Գրանցման տարեթիվ")
    last_updated = models.DateTimeField(verbose_name="Տվ․ թարմացման տարեթիվ")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Նկար", blank=True)

    def __str__(self):
        return self.full_name


class Teacher(Person, models.Model):
    students = models.ManyToManyField('Student', blank=True, verbose_name="Աշակերտներ   ")
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name="Առարկա",
                                related_name='teacher_subject')

    class Meta:
        verbose_name = "Դասատու"
        verbose_name_plural = "Դասատուներ"
        ordering = ['join_date']


class Student(Person, models.Model):
    teachers = models.ManyToManyField('Teacher', blank=True, verbose_name="Դասատուներ")
    subjects = models.ManyToManyField('Subject', blank=True, verbose_name="Առարկաներ")

    class Meta:
        verbose_name = "Աշակերտ"
        verbose_name_plural = "Աշակերտներ"
        ordering = ['join_date']
