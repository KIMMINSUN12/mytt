from django.db import models
class Info(models.Model):
    schoolname = models.CharField(max_length=100) #학교 이름
    semester = models.IntegerField(default=0) #학기
    credit = models.IntegerField(default=0) #학점
    def __str__(self):
        return self.schoolname

class Info2(models.Model):
    major = models.CharField(max_length=200) #주전공
    minor = models.CharField(max_length=200) #복수전공
    elective = models.IntegerField(default=0) #교양
    max_lecture = models.IntegerField(default=0) #연강
    no_class_day = models.CharField(max_length=5) #공강
    def __str__(self):
        return self.major
