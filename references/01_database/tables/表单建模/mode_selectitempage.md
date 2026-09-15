# 泛微OA 数据表: `mode_selectitempage`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_selectitempage`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `selectitemname` | 选择项名称 | `varchar2` | 1000 | 是 | - |
| 3 | `selectitemdesc` | 选择项描述 | `varchar2` | 1000 | 是 | - |
| 4 | `creater` | 创建人 | `integer` | - | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 1000 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 1000 | 是 | - |
| 7 | `appid` | 应用id | `integer` | - | 是 | - |
| 8 | `uuid` | 32位id | `varchar2` | 800 | 是 | - |
| 9 | `operatetime` | 操作时间 | `varchar2` | 160 | 是 | - |
| 10 | `formids` | 关系表单 | `varchar2` | 2000 | 是 | 使用到的表单id |
