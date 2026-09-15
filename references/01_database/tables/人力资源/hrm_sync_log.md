# 泛微OA 数据表: `hrm_sync_log`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_sync_log`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `dataid` | 数据id | `varchar2` | 80 | 是 | 数据id 分部id、部门id、人员id |
| 3 | `outkey` | 外部主键 | `varchar2` | 800 | 是 | 外部主键 |
| 4 | `datatype` | 数据类型 | `integer` | - | 是 | 数据类型 1：分部；2：部门；3：岗位；4：用户 |
| 5 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 7 | `deltype` | 操作类型 | `integer` | - | 是 | 1 新增 2修改 |
