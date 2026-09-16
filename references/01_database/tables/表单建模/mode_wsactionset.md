# 泛微OA 数据表: `mode_wsactionset`

- **中文名称**: WebService Action基础表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_wsactionset`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `actionname` | 接口名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `expandid` | 扩展id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `inpara` | 输入参数 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `actionorder` | 接口顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `wsurl` | 接口url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `wsoperation` | 接口操作 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 9 | `xmltext` | xml描述 | `long` | 0 | 是 | 否 | 否 | - | - | - |
| 10 | `rettype` | 链接类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `retstr` | 链接字段 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
