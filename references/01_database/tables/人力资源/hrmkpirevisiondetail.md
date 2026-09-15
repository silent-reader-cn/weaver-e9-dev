# 泛微OA 数据表: `hrmkpirevisiondetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmkpirevisiondetail`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | ID |
| 2 | `goalid` | 系统模板id | `integer` | - | 是 | 系统模板id |
| 3 | `operator` | 操作者 | `integer` | - | 是 | 操作者 |
| 4 | `operatetime` | 操作时间 | `varchar2` | 160 | 是 | 操作时间 |
| 5 | `operatetype` | 操作类型 | `char` | 1 | 是 | 操作类型 |
| 6 | `clientip` | 客户端ip地址 | `varchar2` | 160 | 是 | 客户端ip地址 |
| 7 | `fieldname` | 修改字段名称 | `varchar2` | 800 | 是 | 修改字段名称 |
| 8 | `originalvalue` | 原始内容 | `varchar2` | 1000 | 是 | 原始内容 |
| 9 | `updatedvalue` | 更新内容 | `varchar2` | 1000 | 是 | 更新内容 |
