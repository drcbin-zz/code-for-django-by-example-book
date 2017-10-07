# Chapter7

## Session

### What is Session

- Session 是为了解决Http无状态而出现的一种技术
- Session 的本质是临时数据的传输与保存


### How session works

- Session 是通过发起请求的时候附带一些数据,一起传输出去.
- 每一个浏览器发出去的session数据都会有一个唯一的session_id
- 服务器可以根据session_id来判断服务器和这个浏览器的一些交互
- 同时,服务器也可以更改session的信息

### How to use session

- 在后台获取 s = request.session
- 对s进行更改
- 调用s.modified=True来通知Django,session已经发生了更改
- 需要查询数据的时候,就查询s


## context_process -- 上下文处理

### 什么是上下文处理

- 上下文处理是连接后台逻辑和前端模板变量的一段python代码,本质是一个函数

### 上下文处理的作用

- 上下文处理可以在request的返回过程中携带或处理一下变量,从而在模板中能使用改变量

### 如何使用上下文处理

- 上下文本质是一段函数代码,函数接受一个request参数,然后一个字典,字典内容便是模板中可以使用的变量名和值
- 将上下文处理函数注册到settings下的template的context_process列表中
- 这样每一个request都能返回携带了自定义处理变量的模板了


## 使用异步任务

### 什么是异步任务

- 当我们写的view函数在处理后台逻辑的时候,是以单线程按流程去处理,而有些东西不必很及时的返回给用户，并且比较耗时。 这时候浏览器就得一直等着，等待响应。 比如发送邮件.
- 异步任务就是脱离当前处理流程,再进行另一个任务.从而不影响当前任务的进行

### 如何使用异步任务

- 自己写逻辑代码实现
- 使用第三方模块实现

### 使用celery实现异步

- 这是书中使用的方式
- 看文档吧...,不写了



## 不使用csrf

### 针对某个视图不用csrf的方法

- 使用装饰器`django.views.decoraters.csrf_exempt`


## django app的初始化顺序以及流程

### django 的app是如何初始化的
 - p261-262有需要.要在ready()方法中import

## 使用自定义admin响应(actions)

### 什么是admin actions

- admin actions 是指在admin界面中,选择了批量的实例之后的可用操作.  比如内置的delete


### 如何使用 admin actions

- 创建action函数
```python
def custom_action(modeladmin, request, queryset):
    """
    queryset: 你在admin视图选择的那些实例
    """

    # do something with quertset

custom_action.short_description = 'Some Description'  # 用于在admin中对外显示
```

- 给Admin添加action

```python
class AnyAdmin(admin.ModelAdmin):
    actions = [custom_action]   # 可以添加多个action
```


## 使用django下载文件

### 核心

- 构造一个response,并且说清楚response['content-type'], 浏览器就会自动识别是显示还是下载



## 在admin中使用自定义template

### 使用方法

- 在admin中使用自定义模版...偏麻烦...  page267
