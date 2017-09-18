# 第4章

## django的认证系统

### 自定义视图来进行认证

- 在视图中正常写认证流程就行, 和正常的业务逻辑一样

### 使用build-in视图进行认证

- 不用自己写view,直接写URL, 然后匹配相应的build-in views就行.
- 需要按规范写模板名字和目录
- 需要在settings.py中配置登录url，登录重定向等。
- 仅仅是少写了views,其他的templates,URL都得自己写



## 使用django的build-in认证流程

### 使用方法

- 可以直接在urls.py中加上 `diango.contrib.auth.urls.patterns`, 然后就可以使用那些账户相关的操作了,如注册,改密等

### 使用注意事项


## django的注册系统

### 用法

- 和认证系统差不多,就是提供的功能不一样
- 一个继承自`forms.ModelForm`的form,可以直接调用foem.save()方法得到一个Model实例



## 扩展build-in User.

#### 给用户添加Profile

- 使用了OneToOneField来将一个用户实例和一个Profile实例关联起来
- 在新注册用户的时候,对新用户实现了自动增加一个Profile
- 对于之前注册的用户,并没有做任何处理, 所以之前的用户不存在Profile，访问会报错



## 使用django messages 系统

### messages系统的作用

- 用于生成一个提醒,并且以上下文的形式返回到模板中,上下文变量为massages,表示消息队列

### messages的使用

- 导入messages
- 在需要返回消息的地方使用messages.XXX(request, 'some messages')
- 在模板中循环遍历messages即可获取每一条消息


## 自定义认证后台

### 什么情况下使用自定义认证

- django的系统只提供了username-password认证
- 更多时候我们邮箱、电话号码等我们贴身的唯一标识认证
- 有时候除了用户名密码，有的地方还需要更加严格的某些东西来辅助认证

### 如何使用自定义认证

- 自定义认证的本质是一段python代码,更严格,其中要有两个方法:get_user(user_id), authenticate(username, password), 当进行认证的时候会调用这两个方法
- 在settings中重写AUTHENTICATION_BACKENDS = ('',''), 会依次从上倒下调用其中的认证，直到某一个认证成功


### 需要注意的

- 书中使用自定义认证来实现了邮箱认证,但是django build-in的User的email并不是唯一的,也就是一个email可能会被两个User使用
- 同样,也可以自定义注册的后台，或者注册的时候要检索邮箱


## 第三方认证

- 由于某些原因,暂时没有实现第三方认证





# 第五章

## 表单数据清洗

### 什么是表单数据清洗

- 传回来的表单可能有一些多余的,也可能会有不合法的，不合规格的等.
- 当我们收到一个表单时,从中提取我们想要的数据,扔掉多余的和不合格的。 这个过程叫做数据清洗

### 如何清洗表单数据

- 当调用form.cleaned_data时,会依次调用每一个form.clean_fieldName的方法.
- 所以,当我们想自定义清洗某一个表单字段的时候,是需要在表单类中定义一个清洗字段的方法就行了


## 表单模型save方法重写




## 使用自定义装饰器

### 构造装饰器

- 装饰器的本质是一段python代码, 用于在执行一段函数之前进行一些验证



# 第六章

## 获取对象url

### 获取对象url的方式

- 在models中定义get_absolute_url
- 在ssettings中定义ABSOLUTE_URL_OVERRIDES, 在书上174页


## 在html中使用data-\*变量

### 什么是data-\*变量

- 该变量的表现形式为一个标签的属性
- 该属性可以存储某个变量,并且该变量可以js直接读取

### data-\*的使用方法

- 在html标签中添加属性`data-varname=value`, 如`<a id="test" data-id="value1" data-other="value2" href="#"></a>`
- 在js中读取变量值:
```html
    $(a#test).data('id')   // value1
    $(a#test).data('other')   // value2
```


## 使用GenericForeignKey

### 什么是GenericForeignKey

- GenericForeignKey是一种通用关系外键,简单说就是这个外键具有通用性,不用确定是什么类型

### 什么情况下使用GenericForeignKey

- 当某个model的外键是个不确定的model的时候.比如评论models的评论对象就不确定是啥

### 如何使用GenericForeignKey

```python3
# 假设我们要做一个评论系统, 有4个model, Music, Book, Movie, Comment

class Music(models.Model):
    name = models.CharField()

    class Meta:
        verboose_name = 'music'

class Book(models.Model):
    name = models.CharField()

    class Meta:
        verboose_name = 'book'

class Movie(models.Model):
    name =  models.CharField()

    class Meta:
        verboose_name = 'movie'

class Comment(models.Model):
    comment_content = models.TextField()
    comment_to = models.ForeignKey(XXX)    # 这里应该怎么写?

# 我们来整理一下我们的处境. 我们在做一个评论系统,现在要做的是将评论和被评论的对象联系起来. 简单的办法就是使用外键. 
# 我以前想到的办法是再定义一个类,CommentAble, 然后

class Comment(models.Model):
    comment_content = models.TextField()
    comment_to = models.ForeignKey(CommentAble)    

class Music(CommentAble):
    pass
class Book(CommentAble):
    pass


# 但这种做法是有弊端的, 首先是没法判断出评论的是什么东西,是Book,Music还是movie。


# django 提供了GenericForeignKey来帮助我们解决这种问题
# 修改代码如下

from django.contrib.contenttype.fields  importGenericForeignKey
from django.contrib.contenttype.models import ContentType
class Comment(models.Model):
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    comment_to = GenericForeignKey('content_type', 'object_id')

# 通过上面的修改, 我们的comment_to就可以是任意类型的外键了

>>> m = Music()
>>> b = Book()
>>> mv = Movie()

# Comment on a music 
>>> c = Comment()
>>> c.comment_to = m
>>> c.save()

# comment on a book
>>> c = Comment()
>>> c.comment_to = m
>>> c.save()

# comment on a movie
>>> c = Comment()
>>> c.comment_to = mv
>>> c.save()


# 简单解释一下: 通常情况下我们只需要知道apple_label,model_name和instance_id就能确定一个instance

# ContentType是一个build-in的对象,他记录了我们所有installed app的所有models. 并形成了一个表,
# 换句话说,就是ContentType已经知道了apple_label和model_name,

# 我们Comment中的content_type就是知道两个条件

# 我们在定义一个object_id来记录instance_id.这样我们就能确定一个实例了

# 我们使用GenericForeignKey将content_type和object_id组合起来,就得到了我们想要的实例



# 当我们有一个Book b,想要查看他的所有comments的情况时呢？

# 先获取实例类型
type = ContentType.objects.get_for_model(b)
# 再过滤出该Model下的instance
Comment.objects.filter(content_type__pk=type.id, object_id=b.id)





# 更方便的办法是使用GenericRelation
# 修改代码如下


from django.contrib.contenttype.fields import GenericRelation
class Music(models.Model):
    ...
    comments = generic.GenericRelation(Comment)



>>> m = Music()
>>> m.comments()

```



## 优化查询

### page 189有优化查询

- 优化方案: 在一次查询中顺带查询往后可能会用到的东西

## 创建动态

### 如何创建动态

- 书中将创建动态的过程封装起来,封装成一个工具,并且封装过程中考虑到出现动态的情况, 除了发起者,还有没有接受者
- 在完成某个操作后,调用发动态的工具


## 使用Signal
