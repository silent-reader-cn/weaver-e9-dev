# 泛微OA 数据表: `monitorguidelog`

- **所属模块**: `版本升级`
- **数据库表名**: `monitorguidelog`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 3 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 4 | `status` | 状态 | `char` | 1 | 是 | 1:显示“切换到运维平台”按钮 |
