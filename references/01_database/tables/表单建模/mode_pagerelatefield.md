# 泛微OA 数据表: `mode_pagerelatefield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_pagerelatefield`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 3 | `hreftype` | 链接目标来源 | `integer` | - | 是 | - |
| 4 | `hrefid` | 链接目标 | `integer` | - | 是 | - |
| 5 | `pageexpandid` | 页面扩展id | `integer` | - | 是 | 对应mode_pageexpand表的id |
