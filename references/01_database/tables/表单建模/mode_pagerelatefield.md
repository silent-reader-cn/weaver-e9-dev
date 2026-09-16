# 泛微OA 数据表: `mode_pagerelatefield`

- **中文名称**: 页面扩展相关字段信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_pagerelatefield`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 3 | `hreftype` | 链接目标来源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `hrefid` | 链接目标 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `pageexpandid` | 页面扩展id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_pageexpand表的id |
