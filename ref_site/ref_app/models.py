from django.db import models

#상품의 종류(고기류,음료 등..)
class Categories(models.Model):
    type= models.CharField(max_length=20)

class Location(models.Model):
    store_location = models.CharField(max_length=20)

#상품 설명
class Product(models.Model):
    name=models.CharField(max_length=20)
    photo=models.ImageField(blank=True,null=True)
    #유통기한
    best_before_date = models.DateTimeField(auto_now_add=True,auto_now=True)
    #상품의 카테고리
    category=models.ForeignKey(Categories)
    #상품의 보관 위치
    location=models.ForeignKey(Location)

#현 보관상태
class Inventory(models.Model):
    #상품 외래키 참조
    product=models.ForeignKey(Product)
    #현 수량
    amount_in=models.IntegerField(default=1)
    #구매날짜
    purchased_date=models.DateTimeField(auto_now_add=True,auto_now=True)

#냉장고 청소
class Cleancheck(models.Model):
    #청소 구역
    location=models.ForeignKey(Location)
    #청소 날짜
    clean_date=models.DateTimeField(auto_now_add=True)

# 냉장고
class Refrigerator(models.Model):
    #냉장고 이름
    name = models.CharField(max_length=30,null=False)
    #보관상태
    inventory = models.ForeignKey(Inventory)
    #오염도
    clean=models.ForeignKey(Cleancheck)

class Memo(models.Model):
    title=models.CharField(max_length=25,null=False)
    content=models.TextField(null=False)
    date=models.DateTimeField(auto_now_add=True,auto_now=True)

class User(models.Model):
    #냉장고 외래키 참조
    gid=models.ForeignKey(Refrigerator)
    #사용자
    id=models.CharField(primary_key=True,max_length=20,null=False)
    #사용자 닉네임
    nickname=models.CharField(max_length=15)
    #장바구니 m:n
    list=models.ManyToManyField(Shopping_list)
    password=models.IntegerField(null=False)
    memo=models.ForeignKey(Memo)

#장바구니
class Shopping_list(models.Model):
    #장바구니 등록자
    user=models.ForeignKey(User)
    product=models.ForeignKey(Product)
    #원하는 구매 수량
    count=models.IntegerField(default=1)
    #상품의 가격
    price=models.IntegerField(default=0)
    # 음식 구매 여부 check .. True or False
    check=models.BooleanField(default=False)




