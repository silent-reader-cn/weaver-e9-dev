# 泛微OA 数据表: `hrm_schedule_personnel`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_schedule_personnel`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `delflag` | 是否删除 | `integer` | - | 否 | 是否删除 |
| 3 | `creater` | 创建人 | `integer` | - | 否 | 创建人 |
| 4 | `create_time` | 创建时间 | `varchar2` | 100 | 否 | 创建时间 |
| 5 | `last_modifier` | 最后修改人 | `integer` | - | 否 | 最后修改人 |
| 6 | `last_modification_time` | 最后修改时间 | `varchar2` | 100 | 否 | 最后修改时间 |
| 7 | `sn` | 排序标识 | `integer` | - | 否 | 排序标识 |
| 8 | `field001` | 类型 | `integer` | - | 否 | 类型 |
| 9 | `field002` | 对象 | `varchar2` | 1000 | 是 | 对象 |
| 10 | `field003` | 安全级别 | `integer` | - | 否 | 安全级别 |
| 11 | `field004` | 安全级别截止 | `integer` | - | 否 | 安全级别截止 |
| 12 | `field005` | 角色级别 | `integer` | - | 否 | 角色级别 |
| 13 | `field006` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 14 | `field007` | 岗位级别范围 | `varchar2` | 100 | 是 | 岗位级别范围 |
