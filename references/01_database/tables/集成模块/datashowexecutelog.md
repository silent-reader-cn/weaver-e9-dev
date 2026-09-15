# 泛微OA 数据表: `datashowexecutelog`

- **所属模块**: `集成模块`
- **数据库表名**: `datashowexecutelog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 自增长主键 |
| 2 | `datashowname` | 自定义浏览框标识 | `varchar2` | 1000 | 是 | 自定义浏览框标识 |
| 3 | `datashowcount` | 自定义浏览框运行次数 | `integer` | - | 是 | 自定义浏览框运行次数 |
| 4 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 5 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 6 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 7 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
