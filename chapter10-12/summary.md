# Chapter 10

## 在admin site中使用Inline

### 什么是Inline

- admin site中的inlines是指在显示一个model信息的时候,一起在该页面显示相关联的model，特别是具有层次关系的多个models之间

### 如何使用Inline

- 以作家(Auth)和书(Book)为例, 将Book嵌入到Auth页面显示
- 在admin.py中.为需要嵌入到另一个model页面的model(子model)编写Inline类

```python

class BookInline(admin.StackedInline):
    model = Book

```
- 在被嵌入的model的admin class中添加inlines

```python
@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    inlines = [BookInline]
```



## 导入导出数据

### 如何导出

- manage.py提供了导出的命令选项
```python3 manage.py dumpdata projectname [--index=2] [--output=path/to/data.json]```

### 如何导出

- manage.py 提供了导入的命令
`python3 manage.py loaddata path/to/data.json`


## 使用通用外键

### 这个在第4-6章有总结



## Django中的model继承

### Abstrac model -- 抽象模型

- 创建模型时,在class Meta中声明  abstract=True

### Proxy model -- 代理模型

- 在创建model时,在class Meta中声明 proxy=True

### 多表继承

- 正常定义models并继承


### 各种继承之间的不同

- 代理模型和抽象模型不会建表,他们和他们的子模型都同时操作同一张表

### 不同继承的选择

- 抽象模型:选择抽象继承的情况大多数为某些东西是抽象的,子模型才能具体实现, 此时选用抽象模型
- 代理模型:选择代理模型的情况是某个模型想具有某种行为或者属性,但是又方便直接添加时,使用代理模型为他做这个事情.
- 多表继承:当子模型和父模型都需要同时存在且互不干扰时选用



## 字段选项 limit_choices_to的用法

### 使用范围

- limit_choices_to 字段选项是针对ForeignKey的.
- choices 是针对CharField的
- limit_choices_to 的值可以是: 字典,Q,返回字段或者Q的可调用对象
- limit_choices_to 的作用: 该外键的选择范围会是Q查询集或者外键中满足键值对过滤出来的


## 使用built-in认证系统

### django提供了内置的认证系统,在第4-6章中有说明


## 使用class-base(基于类)的视图

### 什么是基于类的视图

- 我们之前接触的视图都是基于函数的
- 基于类的视图是将函数封装成类,将原函数中需要用的的变量封装成成员,函数封装成方法

### 为什么使用基于类的视图

- 为了重用: 很多视图的功能逻辑是差不多的,只有其中一小部分改动.把不变的提出来,方便代码重用
- 为了实现更加复杂的功能:基于类,就可以使用面向对象的特征
- 为了方便维护管理



## 使用Mixin

### 什么是mixin

- mixin是python中的一种不知道怎么说的东西.不是语法规定,而是一种规范或者习俗？？？
- mixin的功能是在一个类中实现一种功能.有点类似于java的接口.



### 为什么要使用mixin

- 当某个类需要实现某种功能时,而这个功能又具有通用性.就将这个功能封装成一个类.
- 然后另一个类继承自该功能类,那么该类又具有了功能类的功能

```python
# 实现一个人,狗,鸡会飞的功能

class FlyableMixin(object):
    '''
    define the fly
    '''
    def fly(self, ):
        print('{} flying'.format(self.name))


class Person(FlyableMixin):
    name = 'person'

class Dog(FlyableMixin):
    name = 'dog'


>>> p = Person()
>>> p.fly()
person flying


>>> d = Dog()
>>> d.fly()
dog flying
```



## 使用内置的权限管理

### django admin site 提供了权限管理功能



## 使用formset

### formset是django提供的一个功能,可以在一个页面一次性提交所有的表单,并进行认证
