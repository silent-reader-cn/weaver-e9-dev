# 泛微OA 数据表: `hrmcareerinvite`

- **中文名称**: 人力资源招聘信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerinvite`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `careername` | 职位名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 职位名称 |
| 3 | `careerpeople` | 招聘人数 | `char` | 4 | 是 | 否 | 否 | - | - | 招聘人数 |
| 4 | `careerage` | 年龄 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 年龄 |
| 5 | `careersex` | 性别 | `char` | 1 | 是 | 否 | 否 | - | - | 0: 男；1：女；2：不限 |
| 6 | `careeredu` | 最低教育程度 | `char` | 1 | 是 | 否 | 否 | - | - | 0: 高中<br>1: 中专<br>2: 大专<br>3: 本科<br>4: 硕士研究生<br>5: 博士研究生<br>6: 不限 |
| 7 | `careermode` | 用工方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 用工方式 |
| 8 | `careeraddr` | 工作地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 工作地址 |
| 9 | `careerclass` | 职位种类 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 职位种类 |
| 10 | `careerdesc` | 职位描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 职位描述 |
| 11 | `careerrequest` | 要求 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 要求 |
| 12 | `careerremark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 备注 |
| 13 | `careertype` | 职位类型 | `char` | 1 | 是 | 否 | 否 | - | 0 | 0:热点；1:校园； |
| 14 | `createrid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 创建人id |
| 15 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 创建日期 |
| 16 | `lastmodid` | 最后修改人id | `integer` | - | 是 | 否 | 否 | - | - | 最后修改人id |
| 17 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最后修改日期 |
| 18 | `careerplanid` | 招聘计划id | `integer` | - | 是 | 否 | 否 | - | - | 招聘计划id |
| 19 | `isweb` | 是否网上发布 | `integer` | - | 是 | 否 | 否 | - | 1 | 1:yes; 2:no |
