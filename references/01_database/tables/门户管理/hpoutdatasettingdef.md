# 泛微OA 数据表: `hpoutdatasettingdef`

- **所属模块**: `门户管理`
- **数据库表名**: `hpoutdatasettingdef`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `pattern` | 数据来源类型 | `char` | 1 | 是 | - |
| 3 | `source` | 数据来源 | `varchar2` | 800 | 是 | - |
| 4 | `area` | 内容 | `varchar2` | 1000 | 是 | - |
| 5 | `datakey` | 主键 | `varchar2` | 400 | 是 | - |
| 6 | `eid` | 元素id | `integer` | - | 是 | - |
| 7 | `tabid` | tab页id | `integer` | - | 是 | - |
| 8 | `wsaddress` | 链接地址 | `varchar2` | 1000 | 是 | - |
| 9 | `wsmethod` | 方法 | `varchar2` | 1000 | 是 | - |
| 10 | `wspara` | 参数 | `varchar2` | 1000 | 是 | - |
| 11 | `href` | 地址 | `varchar2` | 1000 | 是 | - |
| 12 | `sysaddr` | 集成登录设置 | `varchar2` | 400 | 是 | - |
