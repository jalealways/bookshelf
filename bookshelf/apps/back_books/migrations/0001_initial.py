# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookBaseInfo',
            fields=[
                ('isbn', models.CharField(db_column='ISBN', max_length=13, primary_key=True, serialize=False)),
                ('book_name', models.CharField(db_column='BOOK_NAME', max_length=100)),
                ('original_proce', models.DecimalField(db_column='ORIGINAL_PROCE', decimal_places=2, max_digits=5)),
                ('author_name', models.CharField(blank=True, db_column='AUTHOR_NAME', max_length=32, null=True)),
                ('translator_name', models.CharField(blank=True, db_column='TRANSLATOR_NAME', max_length=32, null=True)),
                ('publishing_time', models.CharField(blank=True, db_column='PUBLISHING_TIME', max_length=7, null=True)),
                ('book_class_id', models.CharField(blank=True, db_column='BOOK_CLASS_ID', max_length=2, null=True)),
                ('douban_rating', models.DecimalField(blank=True, db_column='DOUBAN_RATING', decimal_places=1, max_digits=2, null=True)),
                ('brief_introduction', models.CharField(blank=True, db_column='BRIEF_INTRODUCTION', max_length=500, null=True)),
                ('cover_pic', models.ImageField(db_column='COVER_PIC', upload_to='static/images/')),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=1, null=True)),
                ('create_time', models.DateTimeField(db_column='CREATE_TIME')),
                ('create_user_id', models.CharField(blank=True, db_column='CREATE_USER_ID', max_length=10, null=True)),
                ('update_time', models.DateTimeField(db_column='UPDATE_TIME')),
                ('update_user_id', models.CharField(blank=True, db_column='UPDATE_USER_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_book_base_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookRating',
            fields=[
                ('rating_id', models.CharField(db_column='RATING_ID', max_length=10, primary_key=True, serialize=False)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=13, null=True)),
                ('reader_rating', models.DecimalField(blank=True, db_column='READER_RATING', decimal_places=1, max_digits=2, null=True)),
                ('reader_comment', models.CharField(blank=True, db_column='READER_COMMENT', max_length=200, null=True)),
                ('reader_id', models.CharField(blank=True, db_column='READER_ID', max_length=10, null=True)),
                ('customer_id', models.CharField(blank=True, db_column='CUSTOMER_ID', max_length=6, null=True)),
                ('rating_time', models.DateTimeField(blank=True, db_column='RATING_TIME', null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=1, null=True)),
                ('original_id', models.CharField(blank=True, db_column='ORIGINAL_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_book_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookshelfBaseInfo',
            fields=[
                ('shelf_id', models.CharField(db_column='SHELF_ID', max_length=10, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, db_column='CUSTOMER_ID', max_length=10, null=True)),
                ('shelf_position', models.CharField(blank=True, db_column='SHELF_POSITION', max_length=100, null=True)),
                ('expire_time', models.DateField(blank=True, db_column='EXPIRE_TIME', null=True)),
                ('total_box_num', models.IntegerField(blank=True, db_column='TOTAL_BOX_NUM', null=True)),
                ('used_box_num', models.IntegerField(blank=True, db_column='USED_BOX_NUM', null=True)),
                ('idled_box_num', models.IntegerField(blank=True, db_column='IDLED_BOX_NUM', null=True)),
                ('create_time', models.DateTimeField(blank=True, db_column='CREATE_TIME', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
            ],
            options={
                'db_table': 'tb_bookshelf_base_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookshelfDetialHis',
            fields=[
                ('sheet_id', models.CharField(db_column='SHEET_ID', max_length=10, primary_key=True, serialize=False)),
                ('box_id', models.CharField(db_column='BOX_ID', max_length=100)),
                ('book_id', models.CharField(blank=True, db_column='BOOK_ID', max_length=10, null=True)),
                ('box_status', models.CharField(blank=True, db_column='BOX_STATUS', max_length=1, null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
            ],
            options={
                'db_table': 'tb_bookshelf_detial_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookStatusDetail',
            fields=[
                ('book_id', models.CharField(db_column='BOOK_ID', max_length=10, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, db_column='CUSTOMER_ID', max_length=10, null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('reader_id', models.CharField(blank=True, db_column='READER_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_book_status_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookStatusDetailHis',
            fields=[
                ('book_id', models.CharField(db_column='BOOK_ID', max_length=10, primary_key=True, serialize=False)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=13, null=True)),
                ('book_status', models.CharField(db_column='BOOK_STATUS', max_length=1)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('reader_id', models.CharField(blank=True, db_column='READER_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_book_status_detail_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCustomerInfo',
            fields=[
                ('customer_id', models.CharField(db_column='CUSTOMER_ID', max_length=10, primary_key=True, serialize=False)),
                ('customer_full_name', models.CharField(blank=True, db_column='CUSTOMER_FULL_NAME', max_length=100, null=True)),
                ('customer_name', models.CharField(blank=True, db_column='CUSTOMER_NAME', max_length=50, null=True)),
                ('cust_addr', models.CharField(blank=True, db_column='CUST_ADDR', max_length=100, null=True)),
                ('emp_number', models.IntegerField(blank=True, db_column='EMP_NUMBER', null=True)),
                ('relation_name', models.CharField(blank=True, db_column='RELATION_NAME', max_length=64, null=True)),
                ('relation_title', models.CharField(blank=True, db_column='RELATION_TITLE', max_length=64, null=True)),
                ('relation_phone', models.CharField(blank=True, db_column='RELATION_PHONE', max_length=11, null=True)),
                ('relation_email', models.CharField(blank=True, db_column='RELATION_EMAIL', max_length=36, null=True)),
            ],
            options={
                'db_table': 'tb_customer_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCustomerOrderInfo',
            fields=[
                ('order_id', models.CharField(db_column='ORDER_ID', max_length=10, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, db_column='CUSTOMER_ID', max_length=10, null=True)),
                ('shelf_id', models.CharField(blank=True, db_column='SHELF_ID', max_length=10, null=True)),
                ('begin_date', models.DateField(blank=True, db_column='BEGIN_DATE', null=True)),
                ('onlime_date', models.DateField(blank=True, db_column='ONLIME_DATE', null=True)),
                ('end_date', models.DateField(blank=True, db_column='END_DATE', null=True)),
                ('order_status', models.CharField(blank=True, db_column='ORDER_STATUS', max_length=1, null=True)),
                ('order_amount', models.BigIntegerField(blank=True, db_column='ORDER_AMOUNT', null=True)),
                ('other_info', models.CharField(blank=True, db_column='OTHER_INFO', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'tb_customer_order_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDicBookStatus',
            fields=[
                ('book_status', models.CharField(db_column='BOOK_STATUS', max_length=2, primary_key=True, serialize=False)),
                ('status_desc', models.CharField(blank=True, db_column='STATUS_DESC', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tb_dic_book_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDicManagerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(blank=True, db_column='ROLE_ID', max_length=4, null=True)),
                ('role_name', models.CharField(blank=True, db_column='ROLE_NAME', max_length=100, null=True)),
                ('authority_desc', models.CharField(blank=True, db_column='AUTHORITY_DESC', max_length=100, null=True)),
                ('create_time', models.DateTimeField(blank=True, db_column='CREATE_TIME', null=True)),
                ('create_user_id', models.CharField(blank=True, db_column='CREATE_USER_ID', max_length=10, null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('update_user_id', models.CharField(blank=True, db_column='UPDATE_USER_ID', max_length=10, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tb_dic_manager_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDicSheetStatus',
            fields=[
                ('sheet_status', models.CharField(db_column='SHEET_STATUS', max_length=1, primary_key=True, serialize=False)),
                ('status_desc', models.CharField(blank=True, db_column='STATUS_DESC', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tb_dic_sheet_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDimBookClass',
            fields=[
                ('child_class_id', models.CharField(db_column='CHILD_CLASS_ID', max_length=2, primary_key=True, serialize=False)),
                ('child_class', models.CharField(blank=True, db_column='CHILD_CLASS', max_length=10, null=True)),
                ('book_class_id', models.CharField(blank=True, db_column='BOOK_CLASS_ID', max_length=2, null=True)),
                ('book_class', models.CharField(blank=True, db_column='BOOK_CLASS', max_length=10, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=1, null=True)),
            ],
            options={
                'db_table': 'tb_dim_book_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbManagerUserInfo',
            fields=[
                ('user_id', models.CharField(db_column='USER_ID', max_length=10, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, db_column='USER_NAME', max_length=30, null=True)),
                ('role_id', models.CharField(blank=True, db_column='ROLE_ID', max_length=4, null=True)),
                ('user_password', models.CharField(blank=True, db_column='USER_PASSWORD', max_length=50, null=True)),
                ('tel_no', models.CharField(blank=True, db_column='TEL_NO', max_length=11, null=True)),
                ('user_status', models.CharField(blank=True, db_column='USER_STATUS', max_length=1, null=True)),
                ('create_tme', models.DateTimeField(blank=True, db_column='CREATE_TME', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('update_user_id', models.CharField(blank=True, db_column='UPDATE_USER_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_manager_user_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbPublishingHouseBaseInfo',
            fields=[
                ('publishing_house_id', models.CharField(db_column='PUBLISHING_HOUSE_ID', max_length=4, primary_key=True, serialize=False)),
                ('publishing_house_name', models.CharField(db_column='PUBLISHING_HOUSE_NAME', max_length=32)),
                ('addr_info', models.CharField(blank=True, db_column='ADDR_INFO', max_length=100, null=True)),
                ('post_no', models.CharField(blank=True, db_column='POST_NO', max_length=6, null=True)),
                ('tel_no', models.CharField(blank=True, db_column='TEL_NO', max_length=12, null=True)),
                ('fax_no', models.CharField(blank=True, db_column='FAX_NO', max_length=16, null=True)),
                ('linkman', models.CharField(blank=True, db_column='LINKMAN', max_length=32, null=True)),
                ('linkman_number', models.CharField(blank=True, db_column='LINKMAN_NUMBER', max_length=11, null=True)),
                ('status', models.CharField(db_column='STATUS', max_length=1)),
                ('create_time', models.DateTimeField(blank=True, db_column='CREATE_TIME', null=True)),
                ('create_user_id', models.CharField(blank=True, db_column='CREATE_USER_ID', max_length=10, null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('update_user_id', models.CharField(blank=True, db_column='UPDATE_USER_ID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_publishing_house_base_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbReaderAuth',
            fields=[
                ('tel_no', models.CharField(db_column='TEL_NO', max_length=11, primary_key=True, serialize=False)),
                ('reader_id', models.CharField(blank=True, db_column='READER_ID', max_length=10, null=True)),
                ('limit_num', models.IntegerField(blank=True, db_column='LIMIT_NUM', null=True)),
            ],
            options={
                'db_table': 'tb_reader_auth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbReaderInfo',
            fields=[
                ('open_id', models.CharField(db_column='OPEN_ID', max_length=100, primary_key=True, serialize=False)),
                ('tel_no', models.CharField(blank=True, db_column='TEL_NO', max_length=11, null=True)),
                ('borrow_limit_num', models.IntegerField(blank=True, db_column='BORROW_LIMIT_NUM', null=True)),
                ('borrow_num', models.IntegerField(blank=True, db_column='BORROW_NUM', null=True)),
                ('borrow_left', models.IntegerField(blank=True, db_column='BORROW_Left', null=True)),
                ('order_limit_num', models.IntegerField(blank=True, db_column='ORDER_LIMIT_NUM', null=True)),
                ('order_num', models.IntegerField(blank=True, db_column='ORDER_NUM', null=True)),
                ('reader_status', models.CharField(blank=True, db_column='READER_STATUS', max_length=1, null=True)),
                ('active_time', models.DateTimeField(blank=True, db_column='ACTIVE_TIME', null=True)),
                ('active_id', models.CharField(blank=True, db_column='ACTIVE_ID', max_length=1, null=True)),
                ('sessionid', models.CharField(blank=True, db_column='SessionID', max_length=10, null=True)),
                ('reg_shelf_id', models.CharField(blank=True, db_column='Reg_shelf_ID', max_length=10, null=True)),
                ('reg_time', models.DateTimeField(blank=True, db_column='Reg_TIME', null=True)),
            ],
            options={
                'db_table': 'tb_reader_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBookshelfBoxInfo',
            fields=[
                ('shelf', models.ForeignKey(db_column='SHELF_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='back_books.TbBookshelfBaseInfo')),
                ('box_id', models.CharField(db_column='BOX_ID', max_length=100)),
                ('book_id', models.CharField(blank=True, db_column='BOOK_ID', max_length=10, null=True)),
                ('box_status', models.CharField(blank=True, db_column='BOX_STATUS', max_length=1, null=True)),
                ('order_open_id', models.CharField(blank=True, db_column='ORDER_OPEN_ID', max_length=10, null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='UPDATE_TIME', null=True)),
                ('raspberry_id', models.CharField(blank=True, db_column='Raspberry_ID', max_length=10, null=True)),
                ('raspberry_status', models.CharField(blank=True, db_column='Raspberry_status', max_length=10, null=True)),
                ('lock_board_id', models.CharField(blank=True, db_column='lock_board_ID', max_length=10, null=True)),
                ('lock_id', models.CharField(blank=True, db_column='lock_ID', max_length=10, null=True)),
                ('lock_status', models.CharField(blank=True, max_length=10, null=True)),
                ('ray_status', models.CharField(blank=True, max_length=10, null=True)),
                ('raspberry_ip', models.CharField(blank=True, db_column='Raspberry_IP', max_length=15, null=True)),
            ],
            options={
                'db_table': 'tb_bookshelf_box_info',
                'managed': False,
            },
        ),
    ]
