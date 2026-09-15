# 泛微OA 数据表: `mode_wsactionset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_wsactionset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `actionname` | 接口名称 | `varchar2` | 1000 | 是 | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | - |
| 4 | `expandid` | 扩展id | `integer` | - | 是 | - |
| 5 | `inpara` | 输入参数 | `varchar2` | 1000 | 是 | - |
| 6 | `actionorder` | 接口顺序 | `integer` | - | 是 | - |
| 7 | `wsurl` | 接口url | `varchar2` | 1000 | 是 | - |
| 8 | `wsoperation` | 接口操作 | `varchar2` | 800 | 是 | - |
| 9 | `xmltext` | xml描述 | `long` | 0 | 是 | - |
| 10 | `rettype` | 链接类型 | `integer` | - | 是 | - |
| 11 | `retstr` | 链接字段 | `varchar2` | 2000 | 是 | - |
