---
layout: post
title:  "postgreSql"
date:   2020-06-12 19:31:29 +0900
category: Database
--- 
# postgreSql

1.  postgresql 설치

```ruby
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```

2.  계정 생성 및 DB 생성

```ruby
-- postgres user로 접근
sudo -i -u postgres

-- psql db로 접근
psql
 
CREATE USER bcadmin WITH PASSWORD '1234';
 
-- 새 데이터베이스(bc_db)의 소유자(bcadmin)가 되게하여 직접 구성하고 관리
CREATE DATABASE bc_db OWNER bcadmin;
 
CREATE SCHEMA bcpaltform AUTHORIZATION bcadmin;

-- public 스키마가 아닌 별도의 스키마를 생성해서 사용하려면 search_path 를 잡아주는 것이 편하다.
-- search_path는 탐색할 스키마의 순서를 지정해주는 변수다.
-- show search_path;
alter USER bcadmin set search_path = 'bcpaltform';
```

3.  테이블, 시퀀스 생성

```ruby
--bcadmin 계정으로 bc_db 데이터베이스에 접근 / 비번 1234
psql -h localhost -U bcadmin -d bc_db

--스키마 생성
CREATE SCHEMA bcpaltform AUTHORIZATION bcadmin;

--시퀀스 생성
CREATE SEQUENCE "menu_id_seq";

--메뉴 생성(id는 위에만든 시퀀스 기반)
CREATE TABLE "menu" (
    "id" INTEGER NOT NULL DEFAULT nextval('menu_id_seq'::regclass), "label" VARCHAR(255) NOT NULL,
    "icon" VARCHAR(50) NULL DEFAULT NULL,
    "link_to" VARCHAR(255) NULL DEFAULT NULL,
    "parent_id" INTEGER NULL DEFAULT NULL,
    "sort_order" INTEGER NULL DEFAULT NULL,
    "use_yn" CHAR(1) NULL DEFAULT 'Y',
    PRIMARY KEY ("id")
);
```

4.  데이터 삽입

```ruby
--OWNED BY 옵션을 사용하면 시퀀스가 특정 테이블 열과 연결되므로
--해당 열 (또는 전체 테이블)이 삭제되면 시퀀스도 자동으로 삭제됩니다.
ALTER SEQUENCE menu_id_seq OWNED BY menu.id;
 
-- organizations 테이블 생성
CREATE TABLE "organizations" (
    "id" UUID NOT NULL,
    "org_name" VARCHAR(255) NOT NULL,
    "org_role" VARCHAR(32) NULL DEFAULT NULL,
    "created_date" TIMESTAMP NULL,
    "modified_date" TIMESTAMP NULL,
    PRIMARY KEY ("id")
);
 
-- users 테이블 생성
CREATE TABLE "users" (
 "id" UUID NOT NULL,
 "email" VARCHAR(128) NOT NULL,
 "password" VARCHAR(128) NOT NULL,
 "user_name" VARCHAR(128) NOT NULL,
 "tel" VARCHAR(20) NULL DEFAULT NULL,
 "org_id" VARCHAR(36) NULL DEFAULT NULL,
 "role" VARCHAR(255)[] NULL,
 "created_date" TIMESTAMP NULL,
 "modified_date" TIMESTAMP NULL,
 "reset_yn" BOOLEAN NULL DEFAULT true,
 PRIMARY KEY ("id")
);
 
-- 인덱스 생성
CREATE UNIQUE INDEX "UNIQUE" ON users(email);
 
-- role_menu 테이블 생성
CREATE TABLE "role_menu" (
    "role_id" VARCHAR(20) NULL DEFAULT NULL,
    "menu_id" INTEGER NULL DEFAULT NULL
);
 
-- role_menu 데이터 삽입
INSERT INTO "role_menu" ("role_id", "menu_id") VALUES ('ADMIN', 30),('ADMIN', 0),('ADMIN', 1),('ADMIN', 2),('ADMIN', 3),('ADMIN', 4),('ADMIN', 10),('ADMIN', 26),('ADMIN', 27),('ADMIN', 9),('ADMIN', 25),('ADMIN', 28),('ADMIN', 7),('ADMIN', 29),('ADMIN', 6),('ADMIN', 5),('ADMIN', 8),('USER', 6),('USER', 7),('USER', 8),('USER', 9),('USER', 5),('GUEST', 9);
 
-- menu 데이터 삽입
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (0, E'시스템관리', E'user', NULL, NULL, 0, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (1, E'회사관리', NULL, E'/admin/company', 0, 1, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (3, E'권한관리', NULL, E'/admin/authority', 0, 3, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (4, E'메뉴관리', NULL, E'/admin/menu', 0, 4, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (2, E'회원관리', NULL, E'/admin/members', 0, 2, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (5, E'예외처리', E'warning', NULL, NULL, 6, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (6, E'403', NULL, E'/error/permission', 5, 7, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (7, E'404', NULL, E'/error/found', 5, 8, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (8, E'500', NULL, E'/error/request', 5, 9, E'Y');
 
INSERT INTO "menu" ("id", "label", "icon", "link_to", "parent_id", "sort_order", "use_yn") VALUES (9, E'PDF Viewer', E'file-pdf', E'/pdf', NULL, 5, E'Y');
 
```