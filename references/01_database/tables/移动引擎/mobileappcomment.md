# 泛微OA 数据表: `mobileappcomment`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappcomment`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `appid` | 应用ID | `integer` | - | 是 | 应用ID |
| 3 | `userid` | 用户ID | `integer` | - | 是 | 用户ID |
| 4 | `score` | 分数 | `integer` | - | 是 | 分数 |
| 5 | `title` | 标题 | `varchar2` | 800 | 是 | 标题 |
| 6 | `content` | 内容 | `varchar2` | 4000 | 是 | 内容 |
| 7 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建日期 |
