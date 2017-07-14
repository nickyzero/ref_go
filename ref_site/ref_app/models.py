from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# 상품의 종류(고기류,음료 등..)
class Categories(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Location(models.Model):
    store_location = models.CharField(max_length=20)

    def __str__(self):
        return self.store_location


# 상품 설명
class Product(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, null=True)
    # 유통기한
    best_before_date = models.DateTimeField(auto_now_add=True)
    # 상품의 카테고리
    category = models.ForeignKey(Categories)
    # 상품의 보관 위치
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name


# 현 보관상태
class Inventory(models.Model):
    # 상품 외래키 참조
    product = models.ForeignKey(Product)
    # 현 수량
    amount_in = models.IntegerField(default=1)
    # 구매날짜
    purchased_date = models.DateTimeField(auto_now_add=True)


# 냉장고 청소
class Cleancheck(models.Model):
    # 청소 구역
    location = models.ForeignKey(Location)
    # 청소 날짜
    clean_date = models.DateTimeField(auto_now_add=True)


# 냉장고
class Refrigerator(models.Model):
    # 냉장고 생성자
    owner = models.ForeignKey(User, null=True)
    # 냉장고 이름
    name = models.CharField(max_length=30, primary_key=True, null=False)
    # 보관상태
    #inventory = models.ForeignKey(Inventory, null=True)
    # 오염도
    #clean = models.ForeignKey(Cleancheck, null=True)

    def __str__(self):
        return self.name


class Memo(models.Model):
    title = models.CharField(max_length=25, null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)


# 장바구니
class Shopping_list(models.Model):
    # 장바구니 등록자
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    # 원하는 구매 수량
    count = models.IntegerField(default=1)
    # 상품의 가격
    price = models.IntegerField(default=0)
    # 음식 구매 여부 check .. True or False
    check = models.BooleanField(default=False)
    def __str__(self):
        return '%s %d %d' % (self.product, self.count, self.price)

# user을 onetoone으로 받는 Setting_user
class Setting_user(models.Model):
    user = models.OneToOneField(User, related_name='user', primary_key=True)
    # 냉장고 외래키 참조
    gid = models.ForeignKey(Refrigerator, null=True)
    # 사용자 닉네임
    nickname = models.CharField(max_length=15, blank=True, default='')
    # 장바구니 m:n
    #list = models.ManyToManyField(Shopping_list, null=True)
    #memo = models.ForeignKey(Memo, null=True)

    def __str__(self):
        return self.user.username


# user생성시 자동으로 Setting_user 생성
def create_setting_user(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        setting_user = Setting_user(user=user)
        setting_user.save()


post_save.connect(create_setting_user, sender=User)