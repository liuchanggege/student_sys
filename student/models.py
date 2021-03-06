from django.db import models

# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1,'男'),
        (2,'女'),
        (0,'未知'),
    ]
    STATUS_ITEMS = [
        (0,'申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128,verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS,verbose_name='性别')
    profession = models.CharField(max_length=128,verbose_name='职业')
    email = models.EmailField(verbose_name='email')
    qq = models.CharField(max_length=128,verbose_name='qq')
    phone = models.CharField(max_length=128,verbose_name='电话')
    status = models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name='审核状态')
    is_delete = models.CharField(max_length=2,default='N',verbose_name='逻辑删除')
    created_time = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='创建时间')#这两个参数干啥的
    updated_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='更新时间')  # 这两个参数干啥的

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<student: %s>'% self.name

    class Meta:
        verbose_name=verbose_name_plural='学员信息'
