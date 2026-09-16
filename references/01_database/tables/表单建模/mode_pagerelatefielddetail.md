# 泛微OA 数据表: `mode_pagerelatefielddetail`

- **中文名称**: 页面扩展相关字段详细设置
- **所属模块**: `表单建模`
- **数据库表名**: `mode_pagerelatefielddetail`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `mainid` | 页面扩展相关字段主id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_pagerelatefield表的id |
| 3 | `modefieldname` | 模块字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `hreffieldname` | 链接目标字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
