from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = verbose_name_plural = '分类'

    def __str__(self, ):
        return self.name

    def get_absolute_url(self, ):
        return reverse('shop:product_list_by_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # db_lindex 就是单独为这个字段再建一个索引表
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )  # 这句的意思是,将这个两个字段一起建成一个索引表,不用单独分类建两个索引表
        verbose_name_plural = verbose_name = u'商品'

    def __str__(self, ):
        return self.name

    def get_absolute_url(self, ):
        return reverse('shop:product_detail', args=[self.id, self.slug])
