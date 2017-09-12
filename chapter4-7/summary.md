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


